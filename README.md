# CodeMMLU

CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding Capabilities

## Overview

CodeMMLU is a comprehensive benchmark designed to evaluate the capabilities of large language models (LLMs) in coding and software knowledge. 
It builds upon the structure of multiple-choice question answering (MCQA) to cover a wide range of programming tasks and domains, including code generation, defect detection, software engineering principles, and much more.


|   	| Subject 	| Topic 	| Size 	|
|:---:	|:---:	|:---:	|:---:	|
| Syntactic knowledge 	| API & Frameworks usage 	| Jquery, Django,   Pandas, Numpy, Scipy 	| 740 	|
|  	|  	| Azure, Git, AWS, svg, xml 	|  	|
|  	|  	| Bootstrap, NodeJS, AngularJS, React, Vue 	|  	|
|  	| Programming language syntax    	| C, C#, C++, Java, Javascript, PHP, Python,  R, Ruby, MatLab, HTML, CSS, TypeScript 	| 6220 	|
| Semantic knowledge 	| DBMS & SQL 	| DBMS, MySQL,   PostgreSQL, SQL 	| 393 	|
|  	| Software principles 	| Data structure & Algorithm 	| 3246 	|
|  	|  	| Object-oriented programming 	|  	|
|  	|  	| Compiler design 	|  	|
|  	|  	| Computer organization and Architecture 	|  	|
|  	|  	| Software Development & Engineering 	|  	|
|  	|  	| System Design 	|  	|
|  	| Others 	| Program accessibility, Computer networks,  Computer science, Cybersecurity, Linux,  Web technologies, AWS 	| 1308 	|
| Real-world task 	| Code completion 	|  	| 163 	|
|  	| Fill in the blank 	|  	| 2129 	|
|  	| Code repair 	|  	| 76 	|
|  	| Defect detection 	|  	| 6006 	|
CodeMMLU benchmark overview structure.


## Leaderboard

| **Family**     | **Model**                   | **Size (B)** | **MMLU** | **GSM8k** | **HumanEval** | **MBPP** | **CodeMMLU** |
|----------------|-----------------------------|--------------|----------|----------|---------------|----------|--------------|
| Anthropic      | Claude-3-sonnet@20240229     | -            | **88.7** | **96.4** | **92.0**      | 76.6     | 55.5         |
| **OpenAI**     | GPT-4o-2024-05-13            | -            | **88.7** | 95.8     | 90.2          | **81.4** | **65.0**     |
|                | GPT-3.5-turbo-1106           | -            | 61.9     | 73.8     | 61.4          | 78.5     | 51.6         |
Closed-source Code MMLU benchmarks.


| **Family**     | **Model**                   | **Size (B)** | **MMLU** | **GSM8k** | **HumanEval** | **MBPP** | **CodeMMLU** |
|----------------|-----------------------------|--------------|----------|----------|---------------|----------|--------------|
| MetaLlama      | Meta-Llama-3,1-70B-Instruct  | 70.0         | **83.6** | **95.1** | 80.5          | 75.4     | 59.7         |
|                | Meta-Llama-3,1-70B           | 70.0         | 79.3     | 83.7     | 58.5          | 66.2     | 40.5         |
|                | Meta-Llama-3-70B             | 70.0         | 79.5     | 83.0     | 48.2          | 70.4     | 49.7         |
|                | Meta-Llama-3-70B-Instruct    | 70.0         | 82.0     | 93.0     | 81.7          | **82.3** | **61.8**     |
|                | CodeLlama-34b-Instruct-hf    | 34.0         | -        | -        | 41.5          | 57.0     | 39.3         |
| Mistral        | Mistral-7B-Instruct-v0.3     | 7.0          | 62.5     | 50.0     | 26.2          | 50.2     | 44.1         |
|                | Mixtral-8x7B-Instruct-v0.1   | 46.7         | 70.6     | 74.4     | 40.2          | 60.7     | 42.7         |
|                | Codestral-22B-v0.1           | 22.0         | -        | -        | 81.1          | 78.2     | 47.6         |
| Phi            | Phi-3-medium-128k-instruct   | 14.0         | 78.0     | 91.0     | 62.2          | 75.2     | 48.7         |
|                | Phi-3-mini-128k-instruct     | 3.8          | 68.8     | 82.5     | 58.5          | 70.0     | 39.2         |
| Qwen           | Qwen2-7B-Instruct            | 7.0          | 70.5     | 82.3     | 79.9          | -        | 51.9         |
|                | Qwen2-57B-A14B-Instruct      | 57.0         | 76.5     | 80.7     | 53.0          | 71.9     | 47.3         |
|                | CodeQwen1.5-7B-Chat          | 7.0          | -        | -        | **83.5**      | 77.7     | 47.7         |
| Yi             | Yi-1.5-34B-Chat              | 34.0         | 67.6     | 71.7     | -             | -        | 50.0         |
|                | Yi-1.5-9B-Chat               | 9.0          | 68.4     | 52.3     | 39.0          | 54.4     | 48.2         |
| DeepSeek       | DeepSeek-coder-7B-instruct-v1.5 | 7.0        | 49.2     | 41.0     | 42.1          | 60.7     | 41.6         |
|                | DeepSeek-coder-33B-instruct  | 33.0         | -        | 60.7     | 79.3          | 70.0     | 37.5         |
|                | DeepSeek-moe-16B-chat        | 16.4         | 45.0     | 18.8     | 26.8          | 39.2     | 31.5         |
|                | DeepSeek-Coder-V2-Lite-Instruct | 16.0      | 60.1     | 86.4     | 81.1          | -        | 47.1         |
| InternLM       | InternLM2.5-20B-chat         | 20.0         | 66.5     | 79.6     | 48.8          | 63.0     | 46.2         |
| StarCoder      | StarCoder2-15B-instruct-v0.1 | 15.0         | -        | -        | 46.3          | 66.2     | 47.8         |

Open-source Code MMLU benchmarks.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Citation
If you find this repository useful, please consider citing our paper:

```
@article{nguyen2024codemmlu,
  title={CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding Capabilities},
  author={Nguyen, Dung Manh and Phan, Thang Chau and Le, Nam Hai and Doan, Thong T. and Nguyen, Nam V. and Pham, Quang and Bui, Nghi D. Q.},
  journal={arXiv preprint},
  year={2024}
}
```