import os
import json
from tqdm import tqdm
from typing import Dict

import torch
from vllm import LLM, SamplingParams
from vllm.lora.request import LoRARequest

from codemmlu.backends.base import Backend

class VllmEngine(Backend):
    def __init__(self, model_name: str, **kwargs):
        super().__init__(model_name=model_name, **kwargs)
        ngpus = torch.cuda.device_count()
        backend_kwargs = dict(
            disable_log_stats=True,
            tensor_parallel_size=ngpus,
            download_dir=self.cache_dir,
            trust_remote_code=self.trust_remote_code,
        )
        
        self.model = LLM(self.model_name, 
            enable_lora=True if self.peft_model else None,
            **backend_kwargs)
        
        self.lora_request = None
        if self.peft_model:
            self.lora_request=LoRARequest("lora", 1, self.peft_model)
            
        self.sampling_params = SamplingParams(
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

    def generate(self):
        result = []
        for batch in tqdm(self.ds_loader, total=len(self.ds_loader), desc="Generating"):
            outputs = self.model.generate(batch['question'], 
                                          self.sampling_params, 
                                          lora_request=self.lora_request)

            batch['generation'] = [output.outputs[0].text for output in outputs]
            result.extend(batch['generation'])
            self._save_result(batch)
            
        self.dataset = self.dataset.add_column('generation', result)
        # TODO: process response and extract answer
        return self.dataset

    def _save_result(self, batched_outputs: Dict):
        assert 'question' in batched_outputs.keys()
        assert 'generation' in batched_outputs.keys()
        
        save_path = os.path.join(self.output_dir, f"{self.subset}.final.generated.jsonl")
        
        with open(save_path, "a") as writer:
            for idx in range(len(batched_outputs['question'])):
                res = dict(
                    task_id=batched_outputs['task_id'][idx],
                    prompt=batched_outputs['question'][idx],
                    response=batched_outputs['generation'][idx]
                )
            
                json.dump(res, writer)
                writer.write("\n")
