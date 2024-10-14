import os
import json
from typing import Dict
from tqdm import tqdm 

from accelerate import Accelerator
from accelerate.utils import gather_object
from transformers import (
    GenerationConfig,
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
    AutoTokenizer
)

from codemmlu.backends.base import Backend

class HuggingfaceEngine(Backend):
    def __init__(self, model_name: str, **kwargs):
        super().__init__(model_name=model_name, **kwargs)
        self.accelerator = Accelerator()

        # TODO: add generation args
        generate_args = dict(
            temperature=self.temperature,
            max_new_tokens=self.max_new_tokens,
        )
        self.generation_config = GenerationConfig(**generate_args)
        
        model_kwargs = dict(
            cache_dir=self.cache_dir,
            trust_remote_code=self.trust_remote_code,
            load_in_8bit=False
        )
        try:
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name, **model_kwargs)
            
        except KeyError: # Except load seq2seq model
            self.model = AutoModelForSeq2SeqLM.from_pretrained(
                self.model_name, **model_kwargs)
        
        if self.peft_model:
            from peft import PeftModel
            self.model = PeftModel.from_pretrained(self.model, self.peft_model)
        
        self.model.to(self.accelerator.device)
        
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name, 
            trust_remote_code=self.trust_remote_code,
            padding_side="left"
        )
        
        if not self.tokenizer.pad_token:
            print("Set EOS_TOKEN to PAD_TOKEN")
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def generate(self) -> str:
        # ``Accelerate`` distribute data and model
        assert self.accelerator

        ds_loader = [self.dataset[i:i+self.batch_size] 
                    for i in range(0, len(self.dataset), self.batch_size)]
        
        for i in range(len(ds_loader)):
            question = ds_loader[i]['question']
            ds_loader[i]['question_ids'] = self.tokenizer(question, return_tensors="pt", padding=True)
        
        result = []
        with self.accelerator.split_between_processes(ds_loader, apply_padding=True) as batched_prompts:
            index = self.accelerator.process_index
            for batch in tqdm(batched_prompts, desc=f"Process: {index} | Generating", position=index):
                input_ids = batch['question_ids'].to(self.accelerator.device)
                outputs = self.model.generate(**input_ids, 
                                            generation_config=self.generation_config,
                                            pad_token_id=self.tokenizer.eos_token_id,
                                            eos_token_id=self.tokenizer.eos_token_id)
                
                outputs = [output[len(prompt) :] for prompt, output in zip(input_ids["input_ids"], outputs)]
                batch_results = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
                
                batch['generation'] = batch_results
                result.extend(batch['generation'])
                self._save_result(batch)
                
        
        result_gather = gather_object(result)[: len(self.dataset)]
        self.dataset = self.dataset.add_column('generation', result_gather)
        # TODO: process response and extract answer
        return self.dataset

    def _save_result(self, batched_outputs: Dict):
        assert 'question' in batched_outputs.keys()
        assert 'generation' in batched_outputs.keys()
        
        if self.accelerator.distributed_type == "MULTI_GPU":
            save_path = os.path.join(self.save_dir, 
                        f"{self.subset}.raw.generated.{self.accelerator.process_index}.jsonl")
        else:
            save_path = os.path.join(self.save_dir, f"{self.subset}.final.generated.jsonl")
        
        with open(save_path, "a") as writer:
            for idx in range(len(batched_outputs['question'])):
                res = dict(
                    task_id=batched_outputs['task_id'][idx],
                    prompt=batched_outputs['question'][idx],
                    response=batched_outputs['generation'][idx]
                )
            
                json.dump(res, writer)
                writer.write("\n")
