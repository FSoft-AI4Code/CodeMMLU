# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The CodeMMLU benchmark."""

import os
import json
from glob import glob

import datasets


_CITATION = """\
@article{nguyen2024codemmlu,
  title={CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding Capabilities},
  author={Nguyen, Dung Manh and Phan, Thang Chau and Le, Nam Hai and Doan, Thong T. and Nguyen, Nam V. and Pham, Quang and Bui, Nghi D. Q.},
  journal={arXiv preprint},
  year={2024}
}
"""

_DESCRIPTION = """\
CodeMMLU is a comprehensive benchmark designed to evaluate the capabilities of large language models (LLMs) in coding and software knowledge
"""

_HOMEPAGE = "https://fsoft-ai4code.github.io/codemmlu/"

_URL = "./data/test"

_SUBJECTS = [
    "programming_syntax", "api_frameworks",
    "software_principles", "dbms_sql", "others",
    "code_completion", "fill_in_the_middle", "code_repair", "defect_detection"
]


class CodeMMLU(datasets.GeneratorBasedBuilder):
    """CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding Capabilities"""
    # Version history:
    # 0.0.1: Initial release.
    VERSION = datasets.Version("0.0.1")

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name=sub, version=datasets.Version("0.0.1"),
            description="CodeMMLU test subject {}".format(sub)
        ) for sub in _SUBJECTS
    ]


    def _info(self):
        features = datasets.Features(
            {
                "task_id": datasets.Value("string"),
                "question": datasets.Value("string"),
                "choices": datasets.features.Sequence(datasets.Value("string")),
            }
        )
        
        if self.config.name == "fill_in_the_middle":
            features["problem_description"] = datasets.Value("string")

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        path = os.path.join(_URL, self.config.name + ".jsonl")
        dl_dir = dl_manager.download(path)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={"data_path": dl_dir},
            ),
        ]

    def _generate_examples(self, data_path):
        """This function returns the examples in the raw (text) form."""
        if data_path.endswith(".jsonl"):
            lines = open(data_path, "r", encoding="utf-8").readlines()
            reader = [json.loads(line) for line in lines]
            for idx, data in enumerate(reader):
                return_dict = {
                    "task_id": data['task_id'],
                    "question": data['question'], 
                    "choices": data['choices'],
                }

                if "fill_in_the_middle" in data_path:
                    return_dict['problem_description'] = data['problem_description']

                yield idx, return_dict
