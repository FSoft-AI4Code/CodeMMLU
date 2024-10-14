zeroshot = """The following are multiple choice questions (with answers) about software development.

Question: {question}
{multiple_choices}

Answer: """

fewshot = """The following are multiple choice questions (with answers) about software development.

Question: If a sorted array of integers is guaranteed to not contain duplicate values, 
in order to search a for a specific value which of the following algorithms is the most efficient for this task?

(A) Bubble Sort (B) Linear Search (C) Insertion Sort (D) Binary Search

Answer: The answer is (D).

Question: {question}
{multiple_choices}

Answer: """

cot_zs = """The following are multiple choice questions (with answers) about software devopment.
 
Question: {question}
{multiple_choices}

Answer: Let's think step by step. """

cot_fs = '''The following are multiple choice questions (with answers) about software devopment.

Question: If a sorted array of integers is guaranteed to not contain duplicate values, in order to search a for a specific value which of the following algorithms is the most efficient for this task?
 
(A) Bubble Sort (B) Linear Search (C) Insertion Sort (D) Binary Search
 
Answer: Let's think step by step. Binary Search is a divide-and-conquer algorithm that works by repeatedly dividing the search interval in half and searching for the value in the appropriate half. Since the array is already sorted and does not contain any duplicate value, this algorithm is optimal to find the desired value. The answer is (D).
 
Question: {question}
{multiple_choices}

Answer: Let's think step by step. '''

GENERAL_PROMPT = dict(zeroshot=zeroshot, 
                      fewshot=fewshot,
                      cot_zs=cot_zs,
                      cot_fs=cot_fs)