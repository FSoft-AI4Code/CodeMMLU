import re
from typing import Optional
from datasets import Dataset, load_dataset

from codemmlu.prompts import GENERAL_PROMPT, CODECOMP_PROMPT, FIM_PROMPT, CODEREPAIR_PROMPT, DEFECT_PROMPT


SEMANTIC_TASK = ["software_principles", "dbms_sql", "others"]

SYNTACTIC_TASK = ["programming_syntax", "api_frameworks"]

REALWORLD_TASK = ["code_completion", "fill_in_the_middle", "code_repair", "defect_detection"]

ALL_TASK = SEMANTIC_TASK + SYNTACTIC_TASK + REALWORLD_TASK + ["all"]


def get_prompt(subset: str, prompt_mode: str) -> str:
    """Get prompt for a given task."""
    assert prompt_mode in ["zeroshot", "fewshot"]

    if subset in SEMANTIC_TASK + SYNTACTIC_TASK:
        return GENERAL_PROMPT[prompt_mode]
    else:
        if subset == "code_completion":
            return CODECOMP_PROMPT[prompt_mode]
        elif subset == "fill_in_the_middle":
            return FIM_PROMPT[prompt_mode]
        elif subset == "code_repair":
            return CODEREPAIR_PROMPT[prompt_mode]
        elif subset == "defect_detection":
            return DEFECT_PROMPT[prompt_mode]
        else:
            raise ValueError(f"Invalid subset: {subset}")


class CodeMMLU:
    """CodeMMLU benchmark loader."""
    TASK_NAME = "codemmlu"
    DATASET_NAME_OR_PATH = "Fsoft-AIC/codemmlu"
    
    def __init__(self, 
                 split: str,
                 subset: str,
                 instruction_prefix: Optional[str] = "",
                 assistant_prefix: Optional[str] = "") -> None:
        
        self.stop_words = ['\n\nQ:', '\n\nQuestion:', '\n\n###', '\n#', "\n<|/", "\n```"]
        self.instruction_prefix = instruction_prefix
        self.assistant_prefix = assistant_prefix
        self.split = split
        self.subset = subset

        self.dataset = load_dataset(self.DATASET_NAME_OR_PATH, subset,
                                    split=split, use_auth_token=True)
        
    
    def prepare_dataset(self, prompt_mode: str="zeroshot") -> Dataset:
        """Preprocess CodeMMLU question.
        
        - Default CodeMMLU prompt is zeroshot. All support prompt modes are:
            - zeroshot
            - fewshot
            - cot_zs (Chain-of-Thought zershot)
            - cot_fs (Chain-of-Thought fewshot)
        """

        TEMPLATE = get_prompt(self.subset, prompt_mode)
            
        def _preprocess(example):
            model_inputs = dict(task_id=[], question=[])
            
            # for idx in range(len(examples[key_column])):
            # question = examples[key_column][idx]
            task_id = example.pop('task_id')
            # MODEL INPUTS HERE
            question = TEMPLATE.format(**example)
            question = self.instruction_prefix + question + self.assistant_prefix
            model_inputs['question'].append(question)
            model_inputs['task_id'] = task_id
            
            return model_inputs
        
        preprocessed_ds = self.dataset.map(_preprocess, 
                                           batched=False,
                                           remove_columns=self.dataset.column_names)
        
        return preprocessed_ds
    
    @staticmethod
    def _stop_at_stop_token(decoded_string, stop_tokens):
        """
        Produces the prefix of decoded_string that ends at the first occurrence of
        a stop_token.
        WARNING: the decoded_string *must not* include the prompt, 
        which may have stop tokens itself.
        """
        min_stop_index = len(decoded_string)
        for stop_token in stop_tokens:
            stop_index = decoded_string.find(stop_token)
            if stop_index != -1 and stop_index < min_stop_index:
                min_stop_index = stop_index
        return decoded_string[:min_stop_index]

    def process_response(self, example):
        answer = self._stop_at_stop_token(example, self.stop_words)
        
        # Substitute special characters with empty string
        answer = re.sub(r'[^A-Za-z0-9 \n]', "", answer)
        processed_answer = []
        for item in answer.splitlines():
            for subitem in item.split(" "):
                if len(subitem) != 1:
                    processed_answer.append(subitem.lower())
                else:
                    processed_answer.append(subitem)
        
        # Concat all the words into a single string
        return ' '.join(processed_answer)

    def parse_answer(self, example):
        """Answer extract function.
        
        Args:
            example (str): The example to extract the answer from
        Returns:
            str: The extracted answer
        """
        extract = re.search(r"answer is (\(*[A-E][\).]*)", example, flags=re.IGNORECASE)
        if extract:
            return extract.group(1).replace("(", "").replace(")", "").replace(".", "").strip()
        
        
        extract = re.search(r"(\(*[A-E][\).]*) is correct", example, flags=re.IGNORECASE)
        if extract:
            return extract.group(1).replace("(", "").replace(")", "").replace(".", "").strip()
        

        match = re.findall(r"(A|B|C|D|E)", example)

        if match:
            # if len(match) > 1:
            #     return None
            return list(match)[0] # Take the first one
        return None