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

_URL = "./test"

_SUBJECTS = [
    "programming_syntax", "api_frameworks",
    "software_principles", "dbms_sql", "others",
    "code_completion", "fill_in_the_middle", "code_repair", "defect_detection"
]


class CodeMMLUConfig(datasets.BuilderConfig):
    """BuilderConfig for SuperGLUE."""

    def __init__(self, features, **kwargs):
        """BuilderConfig for CodeMMLU.
        """
        # Version history:
        # 0.0.1: Initial release.
        super().__init__(version=datasets.Version("0.0.1"), **kwargs)
        self.features = features


class CodeMMLU(datasets.GeneratorBasedBuilder):
    """CodeMMLU: A Multi-Task Benchmark for Assessing Code Understanding Capabilities"""
    BUILDER_CONFIG_CLASS = CodeMMLUConfig
    BUILDER_CONFIGS = []
    for sub in _SUBJECTS:
        features = ['task_id', 'question', 'choices']
        if sub == "fill_in_the_middle":
            features.append('problem_description')
        
        BUILDER_CONFIGS.append(CodeMMLUConfig(
            name=sub, 
            features=features,
            description="CodeMMLU test subject {}".format(sub),
        ))


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
        archive = dl_manager.download(_URL)
        dl_dir = dl_manager.download_and_extract(self.config.data_url) or ""
        task_name = _get_task_name_from_data_url(self.config.data_url)
        dl_dir = os.path.join(dl_dir, task_name)
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={
                    "iter_archive": dl_manager.iter_archive(archive), 
                },
            ),
        ]
    
    def _generate_examples(self, iter_archive):
        """This function returns the examples in the raw (text) form."""
        for path, file in iter_archive:
            if path.endswith(".jsonl"):
                lines = (line.decode("utf-8") for line in file)
                reader = [json.loads(line) for line in lines]
                for data in reader:
                    id_ = data['task_id']

                    return_dict = {
                        "question": data['question'], 
                        "choices": data['choices'],
                    }

                    if "fill_in_the_middle" in path:
                        return_dict['problem_description'] = data['problem_description']

                    yield id_, return_dict
