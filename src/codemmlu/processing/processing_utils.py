import os
import re
import glob
import json


MCQ_STOP_TOKENS = ['\n\nQ:', '\n\nQuestion:', '\n\n###', '\n#']

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


def post_process_answer(example):
    answer = _stop_at_stop_token(example, MCQ_STOP_TOKENS)
    
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

def extract_answer(example):
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