# Copyright 2022 Tellius, Inc
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
from unittest import TestCase

from tellius_data_manager.pipes.pipe import Pipe
from tellius_data_manager.pipes.pipe_factory import PipeFactory


class TestPipeFactory(TestCase):
    def setUp(self) -> None:
        self.__factory = PipeFactory

    def tearDown(self) -> None:
        pass

    def test_generate(self):
        obj = self.__factory.generate(
            configuration={
                "name": "test",
                "config": {
                    "pipe_id": None,
                    "job_id": None,
                },
                "type": "pipe",
            }
        )

        self.assertIsInstance(obj, Pipe)
