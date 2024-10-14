
zeroshot = """The following are multiple choice questions (with answers) about 
programming problem.

Question: Which solution below is the most likely completion the following 
code snippet to achieve the desired goal?
{question}

{multiple_choices}

Answer: """

fewshot = """The following are multiple choice questions (with answers) about 
programming problem.

Question: Which solution below is the most likely completion the following 
code snippet to achieve the desired goal?
```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    
    >>> two_sum([2,7,11,15], 9) 
    [0,1]
    >>> two_sum([3,2,4], 6) 
    [1,2]
    >>> two_sum([3,3], 6) 
    [0,1]
    '''
```
(A) ```python
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```
(B) ```python
    for num in nums:
        if target - num in nums:
            return [nums.index(num), nums.index(target - num)]
    return []
```
(C) ```python
    for i in range(len(nums)):
        if nums[i] * 2 == target:
            return [i, i]
    return []
```
(D) ```python
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[i] = num
    return []
```
Answer: The answer is (A).

Question: Which solution below is the most likely completion the following 
code snippet to achieve the desired goal?
```python
{question}
```

{multiple_choices}

Answer: """

cot_zs = '''The following are multiple choice questions (with answers) about 
programming problem.

Question: Which solution below is the most likely completion the following 
code snippet to achieve the desired goal?
```python
{question}
```
{multiple_choices}

Answer: Let's think step by step. '''

cot_fs = """The following are multiple choice questions (with answers) about 
programming problem.

Question: Which solution below is the most likely completion the following 
code snippet to achieve the desired goal?
```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    
    >>> two_sum([2,7,11,15], 9) 
    [0,1]
    >>> two_sum([3,2,4], 6) 
    [1,2]
    >>> two_sum([3,3], 6) 
    [0,1]
    '''
```
(A) ```python
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```
(B) ```python
    for num in nums:
        if target - num in nums:
            return [nums.index(num), nums.index(target - num)]
    return []
```
(C) ```python
    for i in range(len(nums)):
        if nums[i] * 2 == target:
            return [i, i]
    return []
```
(D) ```python
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[i] = num
    return []
```

Answer: Let's think step by step. The answer (A) uses a straightforward brute-force approach by checking every possible pair of indices to see if their corresponding values sum to the target. While this method has a time complexity of O(n^2), it is simple and guaranteed to find the correct solution for small input sizes, as it exhaustively evaluates all pairs. This solution works reliably within the problem's constraints and ensures the correct indices are returned when the target sum is found. The other solutions have issues such as incorrect handling of duplicate values or incorrect logic (as in C) that disqualify them.
The answer is (A).

Question: Which solution below is the most likely completion the following 
code snippet to achieve the desired goal?
```python
{question}
```
{multiple_choices}

Answer: Let's think step by step. """

CODECOMP_PROMPT = dict(zeroshot=zeroshot, 
                      fewshot=fewshot,
                      cot_zs=cot_zs,
                      cot_fs=cot_fs)