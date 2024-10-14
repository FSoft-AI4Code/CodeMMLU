
zeroshot = """The following are multiple-choice questions (with answers) about debugging a programming problem.

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?
{question}

{multiple_choices}

Answer: """

fewshot = """The following are multiple-choice questions (with answers) about debugging a programming problem.

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?

ABCDEF

Answer: The answer is (A).

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?
{question}

{multiple_choices}

Answer: """

cot_zs = zeroshot + "Let's think step by step. "

cot_fs = """The following are multiple-choice questions (with answers) about debugging a programming problem.

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?

ABCDEF

Answer: Let's think step by step. ABCDEF.
The answer is (A).

Question: The implementation below is producing incorrect results. 
Which solution below correctly identifies the bug and repairs it to achieve the desired goal?
{question}

{multiple_choices}

Answer: Let's think step by step. """

CODECOMP_PROMPT = dict(zeroshot=zeroshot, 
                      fewshot=fewshot,
                      cot_zs=cot_zs,
                      cot_fs=cot_fs)