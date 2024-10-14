from abc import ABC, abstractmethod
from codemmlu.task_utils import CodeMMLU

class Backend(ABC):
    def __init__(self,
        dataset: CodeMMLU,
        model_name: str,
        temperature: float,
        max_new_tokens: int,
        peft_model: str = None,
        batch_size: int = 16,
        trust_remote_code: bool = False,
        instruction_prefix: str = None,
        assistant_prefix: str = None,
        cache_dir: str = None,
        output_dir: str=None):
        print(f"Initializing {self.__class__.__name__} backend")
        print(f"Initializing a decoding model: {model_name}")

        self.model_name = model_name
        self.batch_size = batch_size
        self.peft_model = peft_model
        self.cache_dir = cache_dir
        self.output_dir = output_dir
        self.dataset = dataset
        self.temperature = temperature
        self.max_new_tokens = max_new_tokens
        self.trust_remote_code = trust_remote_code
        self.instruction_prefix = instruction_prefix
        self.assistant_prefix = assistant_prefix

    
    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError

    def get_dataset(self) -> CodeMMLU:
        return self.dataset