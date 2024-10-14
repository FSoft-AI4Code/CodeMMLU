ZEROSHOT_PROMPT = '\n{}\n'

def get_prompt(subset: str, prompt_mode: str) -> str:
    """Get prompt for a given task."""
    if prompt_mode == "zeroshot":
        return ZEROSHOT_PROMPT
    # elif prompt_mode == "fewshot":
    #     return prompt
    else:
        raise ValueError(f"Invalid prompt mode: {prompt_mode}")