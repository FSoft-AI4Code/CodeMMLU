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
    <a href="#-news">📰 News</a> •
    <a href="#-quick-start">🚀 Quick Start</a> •
    <a href="#-evaluation">📋 Evaluation</a> •
    <a href="#-citation">📌 Citation</a>
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
codemmlu --model_name <your_model_name_or_path> \
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

Generating with CodeMMLU questions:
```bash
codemmlu --model_name <your_model_name_or_path> \
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

<details><summary>⏬ API Usage <i>:: click to expand ::</i></summary>
<div>

```bash
codemmlu [-h] [-V] [--subset SUBSET] [--batch_size BATCH_SIZE] [--instruction_prefix INSTRUCTION_PREFIX]
                [--assistant_prefix ASSISTANT_PREFIX] [--output_dir OUTPUT_DIR] [--model_name MODEL_NAME]
                [--peft_model PEFT_MODEL] [--backend BACKEND] [--max_new_tokens MAX_NEW_TOKENS]
                [--temperature TEMPERATURE] [--prompt_mode PROMPT_MODE] [--cache_dir CACHE_DIR] [--trust_remote_code]

==================== CodeMMLU ====================

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         Get version
  --subset SUBSET       Select evaluate subset
  --batch_size BATCH_SIZE
  --instruction_prefix INSTRUCTION_PREFIX
  --assistant_prefix ASSISTANT_PREFIX
  --output_dir OUTPUT_DIR
                        Save generation and result path
  --model_name MODEL_NAME
                        Local path or Huggingface Hub link to load model
  --peft_model PEFT_MODEL
                        Lora config
  --backend BACKEND     LLM generation backend (default: hf)
  --max_new_tokens MAX_NEW_TOKENS
                        Number of max new tokens
  --temperature TEMPERATURE
  --prompt_mode PROMPT_MODE
                        Prompt available: zeroshot, fewshot, cot_zs, cot_fs
  --cache_dir CACHE_DIR
                        Cache for save model download checkpoint and dataset
  --trust_remote_code
```

</div>
</details>


List of supported backends:

| Backend          	| DecoderModel 	| LoRA 	|
|------------------	|--------------	|------	|
| [Transformers](https://github.com/huggingface/transformers) (hf) 	| ✅            | ✅    |
| [Vllm](https://github.com/vllm-project/vllm) (vllm)      	| ✅            | ✅    |

### Leaderboard
To evaluate your model and submit your results to the [leaderboard](https://fsoft-ai4code.github.io/leaderboards/codemmlu/), please follow the instruction in [data/README.md](data/README.md).

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
