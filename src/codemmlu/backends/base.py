from abc import ABC, abstractmethod

class Backend(ABC):
    def __init__(self,
        split: str,
        subset: str,
        model_name: str,
        temperature: float,
        max_new_tokens: int,
        peft_model: str = None,
        trust_remote_code: bool = False,
        instruction_prefix: str = None,
        response_prefix: str = None,
        cache_dir: str = None,
        output_dir: str=None):
        print(f"Initializing {self.__class__.__name__} backend")
        print(f"Initializing a decoding model: {model_name}")

        self.model = model_name
        self.peft_model = peft_model
        self.cache_dir = cache_dir
        self.output_dir = output_dir
        self.split = split
        self.subset = subset
        self.temperature = temperature
        self.max_new_tokens = max_new_tokens
        self.trust_remote_code = trust_remote_code
        self.instruction_prefix = instruction_prefix
        self.response_prefix = response_prefix

    
    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError