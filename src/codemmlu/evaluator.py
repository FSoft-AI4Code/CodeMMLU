"""Evaluator to load CodeMMLU and extract answer from response. 

For example:

.. code-block:: python

    >>> from codemmlu import Evaluator
    >>> evaluator = Evaluator(subset="semantic")
    >>> response = evaluator.generate(temperature=0.9, num_return_sequences=3)

"""
import os
import sys
import json
import time
from warnings import warn
from typing import Optional, Dict, List

import torch

from codemmlu.backends import make_model, SUPPORTED_BACKENDS

class Evaluator:
    """Evaluator class.

        :param model_name: Selected model for evaluating
        :type model_name: str
        :param peft_model: Adapter model, defaults to None
        :type peft_model: Optional[str], optional
        :param trust_remote_code: Huggingface argument, defaults to False
        :type trust_remote_code: Optional[bool], optional
        :param cache_dir: Downloaded cache directory, defaults to None
        :type cache_dir: Optional[str], optional
        :param batch_size: Generation batch size, defaults to 16
        :type batch_size: Optional[int], optional
        :param output_dir: Saving generation directory, defaults to "./output"
        :type output_dir: Optional[str], optional
    """
    
    def __init__(self, 
                 model_name: str,
                 subset: Optional[str] = None,
                 split: Optional[str] = "test",
                 peft_model: Optional[str] = None,
                 backend: str = "hf",
                 trust_remote_code: Optional[bool] = False,
                 cache_dir: Optional[str] = None,
                 batch_size: Optional[int] = 16,
                 output_dir: Optional[str] = "./output",
                 instruction_prefix: Optional[str] = "",
                 assistant_prefix: Optional[str] = "",
                 ) -> None:

        # Dataset args
        self.split = split
        self.subset = subset if subset else "all"
        self.instruction_prefix = instruction_prefix
        self.assistant_prefix = assistant_prefix

        # Generation args
        self.backend = backend
        self.model_name = model_name
        self.peft_model = peft_model
        self.output_dir = output_dir
        self.trust_remote_code = trust_remote_code
        self.cache_dir = cache_dir
        self.batch_size = batch_size

        if backend not in SUPPORTED_BACKENDS:
            raise ValueError(f"Backend {backend} is not supported. Please choose from {SUPPORTED_BACKENDS}")
        
        os.makedirs(self.output_dir, exist_ok=True)

    
    def generate(self,
        max_new_tokens: int = 1024,
        temperature: float = 0.0,
        ) -> List:
        """Start backend, generate and extract answer from response

        :param max_new_tokens: Max new tokens, defaults to 256
        :type max_new_tokens: Optional[int], optional
        :param temperature: Model generate temperature, defaults to 0.9
        :type temperature: Optional[float], optional
        
        :return: List of generated result, stored in dictionary object 
            with ``task_id``, ``prompt`` and ``answer`` key.
        :rtype: List
        """
        print(f"Evaluating task: [{self.TASK_NAME}]")
        print(f"pt={torch.__version__}, cuda={torch.version.cuda}, nccl={torch.cuda.nccl.version()}")
        print(f"device compute capabilities={torch.cuda.get_device_capability()}")
        print(f"pytorch compute capabilities={torch.cuda.get_arch_list()}")

        self.engine = make_model(
            split=self.split,
            subset=self.subset,
            model_name=self.model_name,
            backend=self.backend,
            peft_model=self.peft_model,
            trust_remote_code=self.trust_remote_code,
            batch_size=self.batch_size,
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            cache_dir=self.cache_dir,
        )
        start_time = time.time()
        results = self.engine.generate()
        
        print("=======  Finished {}  =======".format(self.TASK_NAME))
        print("Completion time: %d s", (time.time() - start_time))
        
        return results
