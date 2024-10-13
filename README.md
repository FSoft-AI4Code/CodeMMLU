# CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding Capabilities

<center>
<img src="asset/code_mmlu_banner.png" alt="CodeMMLU">
</center>

<p align="center">
    <a href="https://fsoft-ai4code.github.io/leaderboards/codemmlu/"><img src="https://custom-icon-badges.demolab.com/badge/Leaderboard-orange?style=flat&logo=barchart&label=%20"></a>
    <a href="https://huggingface.co/collections/bigcode/bigcodebench-666ed21a5039c618e608ab06"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Datasets-CodeMMLU-f9a602?style=flat"></a>
    <a href="https://fsoft-ai4code.github.io/codemmlu/"><img src="https://custom-icon-badges.demolab.com/badge/WebPage-1a4f76?style=flat&logo=web"></a>
    <a href="https://arxiv.org/abs/2406.15877"><img src="https://img.shields.io/badge/2410.01999-red?style=flat&label=arXiv"></a>
    <!-- <a href="https://pypi.org/project/bigcodebench/"><img src="https://img.shields.io/pypi/v/bigcodebench?color=g"></a> -->
    <!-- <a href="https://pepy.tech/project/bigcodebench"><img src="https://static.pepy.tech/badge/bigcodebench"></a> -->
    <a href="https://github.com/bigcodebench/bigcodebench/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
    <!-- <a href="https://hub.docker.com/r/bigcodebench/bigcodebench-evaluate" title="Docker-Eval"><img src="https://img.shields.io/docker/image-size/bigcodebench/bigcodebench-evaluate"></a>
    <a href="https://hub.docker.com/r/bigcodebench/bigcodebench-generate" title="Docker-Gen"><img src="https://img.shields.io/docker/image-size/bigcodebench/bigcodebench-generate"></a> -->
</p>

<p align="center">
    <!-- <a href="#-impact">💥 Impact</a> • -->
    <a href="#-news">📰 News</a> •
    <a href="#-quick-start">🔥 Quick Start</a> •
    <a href="#-evaluation">🚀 Evaluation</a> •
    <!-- <a href="#-llm-generated-code">💻 LLM-generated Code</a> • -->
    <a href="#-citation">📜 Citation</a>
</p>

## About

### CodeMMLU

CodeMMLU is a comprehensive benchmark designed to evaluate the capabilities of large language models (LLMs) in coding and software knowledge. 
It builds upon the structure of multiple-choice question answering (MCQA) to cover a wide range of programming tasks and domains, including code generation, defect detection, software engineering principles, and much more.

### Why CodeMMLU?

## News
**[2024-10-13]** We are releasing CodeMMLU benchmark v0.0.1 and preprint [HERE](https://arxiv.org/abs/2406.15877)!

## Quick Start

Install CodeMMLU and setup dependencies via `pip`:
```bash
pip install codemmlu
```

Generate response for CodeMMLU MCQs benchmark:
```bash
code_mmlu.generate --model_name_or_path <your_model_name_or_path> \
--subset [semantic|syntactic|realtask] \
--output_dir <your_output_dir> \
--backend [vllm|hf|anthropic|openai]
```


## Evaluation


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
