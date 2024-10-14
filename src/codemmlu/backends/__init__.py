from codemmlu.backends.base import Backend
from codemmlu.task_utils import CodeMMLU

SUPPORTED_BACKENDS = ["vllm", "hf"]

def make_model(
    model_name: str,
    backend: str,
    subset: str,
    split: str,
    temperature: float = 0.0,
    max_new_tokens: int = 1280,
    # instruction model only
    instruction_prefix: str = None,
    assistant_prefix: str = None,
    trust_remote_code: bool = False,
    # peft model only
    peft_model: str = None,
    # cache dir
    cache_dir: str = None
) -> Backend:
    # Load dataset
    dataset = CodeMMLU(subset=subset, split=split)

    # Initialize backend
    if backend == "vllm":
        from codemmlu.backends.vllm import VllmEngine

        return VllmEngine(
            model_name=model_name,
            peft_model=peft_model,
            dataset=dataset,
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            instruction_prefix=instruction_prefix,
            assistant_prefix=assistant_prefix,
            cache_dir=cache_dir
        )
    elif backend == "hf":
        from codemmlu.backends.hf import HuggingfaceEngine

        return HuggingfaceEngine(
            model_name=model_name,
            peft_model=peft_model,
            dataset=dataset,
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            instruction_prefix=instruction_prefix,
            assistant_prefix=assistant_prefix,
            trust_remote_code=trust_remote_code,
            cache_dir=cache_dir
        )
    else:
        raise ValueError(f"Unknown backend: {backend}")