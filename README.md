# CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding Capabilities

<center>
<img src="asset/code_mmlu_banner.png" alt="CodeMMLU">
</center>

<p align="center">
    <a href="https://fsoft-ai4code.github.io/leaderboards/codemmlu/"><img src="https://custom-icon-badges.demolab.com/badge/Leaderboard-orange?style=flat&logo=barchart&label=%20"></a>
    <a href="https://huggingface.co/datasets/Fsoft-AIC/CodeMMLU"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Datasets-CodeMMLU-f9a602?style=flat"></a>
    <a href="https://fsoft-ai4code.github.io/codemmlu/"><img src="https://custom-icon-badges.demolab.com/badge/WebPage-1a4f76?style=flat&logo=web"></a>
    <a href="https://arxiv.org/abs/2406.15877"><img src="https://img.shields.io/badge/2410.01999-red?style=flat&label=arXiv"></a>
    <a href="https://pypi.org/project/codemmlu/"><img src="https://img.shields.io/pypi/v/codemmlu?color=g"></a>
    <!-- <a href="https://pepy.tech/project/bigcodebench"><img src="https://static.pepy.tech/badge/bigcodebench"></a> -->
    <a href="https://github.com/bigcodebench/bigcodebench/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
    <!-- <a href="https://hub.docker.com/r/bigcodebench/bigcodebench-evaluate" title="Docker-Eval"><img src="https://img.shields.io/docker/image-size/bigcodebench/bigcodebench-evaluate"></a>
    <a href="https://hub.docker.com/r/bigcodebench/bigcodebench-generate" title="Docker-Gen"><img src="https://img.shields.io/docker/image-size/bigcodebench/bigcodebench-generate"></a> -->
</p>

<p align="center">
    <!-- <a href="#-impact">💥 Impact</a> • -->
    <a href="#📰-news">📰 News</a> •
    <a href="#🚀-quick-start">🚀 Quick Start</a> •
    <a href="#📋-evaluation">📋 Evaluation</a> •
    <!-- <a href="#-llm-generated-code">💻 LLM-generated Code</a> • -->
    <a href="#📌-citation">📌 Citation</a>
</p>

## 📌 About

### CodeMMLU

**CodeMMLU** is a comprehensive benchmark designed to evaluate the capabilities of large language models (LLMs) in coding and software knowledge. 
It builds upon the structure of multiple-choice question answering (MCQA) to cover a wide range of programming tasks and domains, including code generation, defect detection, software engineering principles, and much more.

### Why CodeMMLU?

- **CodeMMLU** comprises over 10,000 questions curated from diverse, high-quality sources. It covers a wide spectrum of software knowledge, including general QA, code generation, defect detection, and code repair across various domains and more than 10 programming languages.

- **Precise and comprehensive:** Checkout our [LEADERBOARD](https://fsoft-ai4code.github.io/leaderboards/codemmlu/) for latest LLM rankings.

## 📰 News
**[2024-10-13]** We are releasing CodeMMLU benchmark v0.0.1 and preprint report [HERE](https://arxiv.org/abs/2406.15877)!

## 🚀 Quick Start

Install CodeMMLU and setup dependencies via `pip`:
```bash
pip install codemmlu
```

Generate response for CodeMMLU MCQs benchmark:
```bash
code_mmlu.generate --model_name <your_model_name_or_path> \
  --subset <subset> \
  --backend <backend> \
  --output_dir <your_output_dir>
```


## 📋 Evaluation

Build `codemmlu` from source:
```bash
git clone https://github.com/Fsoft-AI4Code/CodeMMLU.git
cd CodeMMLU
pip install -e .
```

> [!Note]
>
> If you prefer `vllm` backend, we highly recommend you install [vllm from official project](https://github.com/vllm-project/vllm/) before install `codemmlu`.

Start evaluating your model via `codemmlu`:
```bash
code_mmlu.generate \
  --model_name <your_model_name_or_path> \
  --peft_model <your_peft_model_name_or_path> \
  --subset all \
  --batch_size 16 \
  --backend [vllm|hf] \
  --max_new_tokens 1024 \
  --temperature 0.0 \
  --output_dir <your_output_dir> \
  --instruction_prefix <special_prefix> \
  --assistant_prefix <special_prefix> \
  --cache_dir <your_cache_dir>
```

List of CodeMMLU subset:

| Subject           	| Subset              	|
|-------------------	|---------------------	|
| Syntactic test    	| programming_syntax  	|
|                   	| api_frameworks      	|
| Semantic test     	| software_principles 	|
|                   	| dbms_sql            	|
|                   	| others              	|
| Realworld problem 	| code_completion     	|
|                   	| fill_in_the_middle  	|
|                   	| code_repair         	|
|                   	| defect_detection    	|

List of supported backends:

| Backend          	| DecoderModel 	| LoRA 	|
|------------------	|--------------	|------	|
| [Transformers](https://github.com/huggingface/transformers)
 (hf) 	| ✅            | ✅    |
| [Vllm](https://github.com/vllm-project/vllm) (vllm)      	| ✅            | ✅    |

## 📌 Citation
If you find this repository useful, please consider citing our paper:

```
@article{nguyen2024codemmlu,
  title={CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding Capabilities},
  author={Nguyen, Dung Manh and Phan, Thang Chau and Le, Nam Hai and Doan, Thong T. and Nguyen, Nam V. and Pham, Quang and Bui, Nghi D. Q.},
  journal={arXiv preprint},
  year={2024}
}
```
