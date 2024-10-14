zeroshot = """The following are multiple-choice questions (with answers) about a programming problem with incomplete solution.

Problem statement: {question}

Incomplete Solution:
{codebase}

Question: The provided solution is missing a part, Which option below is the most likely to complete the solution and achieve the desired goal?

{multiple_choices}

Answer: """

fewshot = """The following are multiple-choice questions (with answers) about a programming problem with incomplete solution.

Problem statement: You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique. 
The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. 
Note that i may equal j. Return an array of right interval indices for each interval i. 
If no right interval exists for interval i, then put -1 at index i.

Incomplete Solution:
python```
def find_right_interval(intervals):
    n = len(intervals)
    res = [-1] * n
    for i in range(n):
        intervals[i].append(i)

    def binary_search(ele):
        left, right = 0, n-1
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] >= ele:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans
            
    intervals.sort()
    for i in intervals:
        _________________

    return res
```

Question: The provided solution is missing a part, Which option below is the most likely to complete the solution and achieve the desired goal?

(A) ```python
    val = binary_search(i[1])
    if val != float('inf'):
        res[i[2]] = intervals[val][2]
```
(B) ```python
    if val != float('inf'): 
        res[i[2]] = intervals[val][2]
    else:
        continue
```
(C) ```python
    val = binary_search(i[1])
		if val != float('inf'): res[i[2] + 1] = intervals[val][2]
```
(D) ```python
    if val != float('inf'): 
			  res[i[2]] = intervals[val][2]
		else:
		  continue
```

Answer: The answer is (A).

Problem statement: {question}

Incomplete Solution:
{codebase}

Question: The provided solution is missing a part, Which option below is the most likely to complete the solution and achieve the desired goal?

{multiple_choices}

Answer: """

cot_zs = """The following are multiple-choice questions (with answers) about a programming problem with incomplete solution.

Problem statement: {question}

Incomplete Solution:
{codebase}

Question: The provided solution is missing a part, Which option below is the most likely to
complete the solution and achieve the desired goal?

{multiple_choices}

Answer: Let's think step by step. """

cot_fs = """The following are multiple-choice questions (with answers) about a programming problem
with incomplete solution.

Problem statement: You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique. 
The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. 
Note that i may equal j. Return an array of right interval indices for each interval i. 
If no right interval exists for interval i, then put -1 at index i.

Incomplete Solution:
python```
def find_right_interval(intervals):
    n = len(intervals)
    res = [-1] * n
    for i in range(n):
        intervals[i].append(i)

    def binary_search(ele):
        left, right = 0, n-1
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] >= ele:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans
            
    intervals.sort()
    for i in intervals:
        _________________

    return res
```

Question: The provided solution is missing a part, Which option below is the most likely to
complete the solution and achieve the desired goal?

(A) ```python
    val = binary_search(i[1])
    if val != float('inf'):
        res[i[2]] = intervals[val][2]
```
(B) ```python
    if val != float('inf'): 
        res[i[2]] = intervals[val][2]
    else:
        continue
```
(C) ```python
    val = binary_search(i[1])
		if val != float('inf'): res[i[2] + 1] = intervals[val][2]
```
(D) ```python
    if val != float('inf'): 
			  res[i[2]] = intervals[val][2]
		else:
		  continue
```

Answer: Let's think step by step. The incomplete solution first sorts the intervals and then iterates over the sorted intervals. For each interval, it finds the right interval using a binary search.
This option (A) finds the right interval index using the binary search and updates the result array accordingly.
The option (B) is similar to (A), but it does not increment the index when finding the right interval index. This could lead to incorrect results.
The option (C) increments the index when finding the right interval index. However, this is incorrect because the problem statement asks for the index of the right interval, not the offset from the original index.
The option (D) uses the same index for both the original interval and the right interval, which could lead to incorrect results.
The answer is (A).

Problem statement: {question}

Incomplete Solution:
{codebase}

Question: The provided solution is missing a part, Which option below is the most likely to
complete the solution and achieve the desired goal?

{multiple_choices}

Answer: Let's think step by step. """

FIM_PROMPT = dict(zeroshot=zeroshot, 
                    fewshot=fewshot,
                    cot_zs=cot_zs,
                    cot_fs=cot_fs)