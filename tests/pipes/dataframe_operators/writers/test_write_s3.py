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
import os
import warnings
from unittest import TestCase

import pandas as pd

from tellius_data_manager.dataframe_operators.writers.s3_csv_writer import S3CSVWriter
from tellius_data_manager.dataframe_operators.writers.dataframe_writer import (
    DataframeWriter,
)


class TestWriteS3(TestCase):
    def setUp(self) -> None:
        test_config = {
            # 'name': 'Test S3 Write',
            "bucket": "genpact-dev",
            "secrets": {"name": "S3", "type": "yamlconfigreader"},
        }

        self._writer = S3CSVWriter(**test_config)

    def tearDown(self) -> None:
        del self._writer

    def test_cotr(self):
        self.assertIsInstance(self._writer, DataframeWriter)
        self.assertEqual(self._writer._bucket, "genpact-dev")

    def test_secrets(self):
        self.assertIsNotNone(self._writer._secrets.access_key_id)
        self.assertIsNotNone(self._writer._secrets.secret_access_key_id)

    def test_write(self):
        test_file = os.path.join("test_data", "test.csv")
        df = pd.read_csv(test_file)
        self._writer.execute(df=df, filename="test_file")
