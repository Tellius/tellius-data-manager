import os
from unittest import TestCase

import pandas as pd

from tellius_data_manager.dataframe_operators.writers.s3_csv_writer import S3CSVWriter
from tellius_data_manager.pipes.pipe import Pipe
from tellius_data_manager.pipes.pipe_status import PipeStatus
from tellius_data_manager.pipes.writers.s3_writer import S3Writer


class TestWriteS3(TestCase):
    def setUp(self) -> None:
        test_config = {
            "name": "Test S3 Write",
            "parents": None,
            "writer": {
                "bucket": "genpact-dev",
                "secrets": {"name": "S3", "type": "yamlconfigreader"},
            },
        }

        self._writer = S3Writer(**test_config)

        test_file = os.path.join("test_data", "test.csv")
        df = pd.read_csv(test_file)

        parent = Pipe()
        parent._state.update_metadata("data", df)
        parent.status = PipeStatus.SUCCESS

        self._writer.parents = [parent]

    def tearDown(self) -> None:
        pass

    def test_cotr(self):
        self.assertEqual(self._writer.name, "Test S3 Write")

    def test_df_operator(self):
        self.assertIsInstance(self._writer._writer, S3CSVWriter)

    def test_write(self):
        self._writer.run(filename="testing/test_file.csv")
