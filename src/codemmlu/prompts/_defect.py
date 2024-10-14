zeroshot = """The following are multiple choice questions (with answers) about programming problem.

Question: Given a code snippet below, which behavior most likely to occur when execute it?
{question}

{multiple_choices}

Answer: """

fewshot = """The following are multiple choice questions (with answers) about programming problem.

Question: Given a code snippet below, which behavior most likely to occur when execute it?
```python
def chkPair(A, size, x):
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (A[i] + A[j] == x):
                return 1
    return 0

```

(A). The code contain no issue.
(B). Memory Limit Exceeded
(C). Internal error
(D). Runtime Error

Answer: The answer is (A).

Question: Given a code snippet below, which behavior most likely to occur when execute it?
{question}

{multiple_choices}

Answer: """

cot_zs = zeroshot + "Let's think step by step. "

cot_fs = """The following are multiple choice questions (with answers) about programming problem.

Question: Given a code snippet below, which behavior most likely to occur when execute it?
```python
def chkPair(A, size, x):
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (A[i] + A[j] == x):
                return 1
    return 0

```

(A). The code contain no issue.
(B). Memory Limit Exceeded
(C). Internal error
(D). Runtime Error

Answer: Let's think step by step. The code defines a function `chkPair` that checks for a pair of elements in an array A whose sum equals x. It uses two nested loops to iterate over all possible pairs and returns 1 if a valid pair is found, or 0 otherwise. The function has a time complexity of O(n^2) due to the nested loops, which could slow down performance for large inputs, but it doesn't involve excessive memory usage or problematic operations that would lead to errors like memory limit exceeded, runtime errors, or internal issues. Hence, the most likely outcome is that the code contains no issue.
The answer is (A).

Question: Given a code snippet below, which behavior most likely to occur when execute it?
{question}

{multiple_choices}

Answer: Let's think step by step."""

DEFECT_PROMPT = dict(zeroshot=zeroshot, 
                      fewshot=fewshot,
                      cot_zs=cot_zs,
                      cot_fs=cot_fs)