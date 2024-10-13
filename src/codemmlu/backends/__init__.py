from codemmlu.backends.base import Backend

def make_model(
    model: str,
    backend: str,
    subset: str,
    split: str,
    dataset: str = "Fsoft-AIC/codemmlu",
    temperature: float = 0.0,
    max_new_tokens: int = 1280,
    # instruction model only
    instruction_prefix: str = None,
    response_prefix: str = None,
    trust_remote_code: bool = False,
    # peft model only
    peft_model: str = None,
    # cache dir
    cache_dir: str = None
) -> Backend:
    if backend == "vllm":
        from codemmlu.backends.vllm import VllmEngine

        return VllmEngine(
            name=model,
            peft_model=peft_model,
            subset=subset,
            dataset=dataset,
            split=split,
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            instruction_prefix=instruction_prefix,
            response_prefix=response_prefix,
            cache_dir=cache_dir
        )
    elif backend == "hf":
        from codemmlu.backends.hf import HuggingfaceEngine

        return HuggingfaceEngine(
            name=model,
            peft_model=peft_model,
            subset=subset,
            split=split,
            dataset=dataset,
            temperature=temperature,
            max_new_tokens=max_new_tokens,
            instruction_prefix=instruction_prefix,
            response_prefix=response_prefix,
            trust_remote_code=trust_remote_code,
            cache_dir=cache_dir
        )
    else:
        raise ValueError(f"Unknown backend: {backend}")