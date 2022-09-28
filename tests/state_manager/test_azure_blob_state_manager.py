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
import datetime
import uuid
from unittest import TestCase

from tellius_data_manager.pipes.pipe_status import PipeStatus
from tellius_data_manager.state_manager.azure_blob_state_manager import (
    AzureBlobStateManager,
)


class TestAzureBlobStateManager(TestCase):
    def setUp(self) -> None:
        self._pipeline_name = "Test Pipeline"
        self._writer_config = {
            "container": "test-state-manager",
            "secrets": {
                "name": "Azure Blob Test",
                "type": "yamlconfigreader",
            },
        }

        self._reader_config = {
            "container": "test-state-manager",
            "secrets": {
                "name": "Azure Blob Test",
                "type": "yamlconfigreader",
            },
        }

        self._test_instance = AzureBlobStateManager(
            **{
                "pipeline_name": self._pipeline_name,
                "state_object_name": "Test Object",
                "name": "Test",
                "version": 1,
                "writer": self._writer_config,
                "reader": self._reader_config,
                "job_id": "123456",
            }
        )

    def tearDown(self) -> None:
        pass

    def test_cotr(self):
        self.assertIsInstance(
            AzureBlobStateManager(
                **{
                    "state_object_name": "Test Object",
                    "name": "Test",
                    "version": 1,
                    "writer": self._writer_config,
                    "reader": self._reader_config,
                }
            ),
            AzureBlobStateManager,
        )

    def test_update(self):
        result = self._test_instance.update(
            start_time=int(datetime.datetime.now().timestamp()),
            stop_time=int(datetime.datetime.now().timestamp() + 100),
            status=PipeStatus.SUCCESS,
            flow_model={},
            push_stats={},
            pull_stats={},
            meta_state={},
        )
        print(result.state)

        result = self._test_instance.update(
            start_time=int(datetime.datetime.now().timestamp()),
            stop_time=int(datetime.datetime.now().timestamp() + 100),
            status=PipeStatus.SUCCESS,
            flow_model={},
            push_stats={},
            pull_stats={},
            meta_state={},
            job_id=uuid.uuid4().hex,
        )
        print(result.state)

    def test_read(self):
        result = self._test_instance.read()
        print(result.state)
