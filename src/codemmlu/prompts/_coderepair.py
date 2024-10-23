
zeroshot = """The following are multiple-choice questions (with answers) about debugging a programming problem.

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?
{question}

{choices}

Answer: """

fewshot = """The following are multiple-choice questions (with answers) about debugging a programming problem.

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?

1 def two_sum(nums, target):
2     complement_map = {{}}    
3     for i, num in enumerate(nums):
4         complement = target - num
5         complement_map[num] = i
6         if complement in complement_map:
7             return [complement_map[complement], i]  
8     return None

(A) Remove line 5.

(B) Remove line 5. Add at line 7:
```        complement_map[num] = i```

(C) Modify line 7:
```         return [i, complement_map[complement]]```

(D) Remove line 5. Add at line 7:
```     if i == len(nums) - 1:
            return None
        complement_map[num] = i```

Answer: The answer is (B).

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?
{question}

{choices}

Answer: """

cot_zs = zeroshot + "Let's think step by step. "

cot_fs = """The following are multiple-choice questions (with answers) about debugging a programming problem.

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?

1 def two_sum(nums, target):
2     complement_map = {{}}  
3     for i, num in enumerate(nums):
4         complement = target - num
5         complement_map[num] = i
6         if complement in complement_map:
7             return [complement_map[complement], i]  
8     return None

(A) Remove line 5.

(B) Remove line 5. Add at line 7:
```        complement_map[num] = i```

(C) Modify line 7:
```         return [i, complement_map[complement]]```

(D) Remove line 5. Add at line 7:
```     if i == len(nums) - 1:
            return None
        complement_map[num] = i```

Answer: Let's think step by step. The bug in the code occurs because the current number is added to the complement_map before checking if its complement already exists, which can lead to incorrectly matching a number with itself. To fix this, the number should only be added to the map after checking for its complement. Solution (B) does exactly this by moving the line that adds the current number to the map after the complement check, ensuring the logic works as intended without self-matching errors.
The answer is (B).

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?
{question}

{choices}

Answer: Let's think step by step. """

CODEREPAIR_PROMPT = dict(zeroshot=zeroshot, 
                      fewshot=fewshot,
                      cot_zs=cot_zs,
                      cot_fs=cot_fs)