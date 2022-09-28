import os
import warnings
from unittest import TestCase

import pandas as pd

from tellius_data_manager.dataframe_operators.writers.azure_blob_csv_writer import (
    AzureBlobCSVWriter,
)
from tellius_data_manager.dataframe_operators.writers.s3_csv_writer import S3CSVWriter
from tellius_data_manager.dataframe_operators.writers.dataframe_writer import (
    DataframeWriter,
)


class TestWriteAzureBlob(TestCase):
    def setUp(self) -> None:
        test_config = {
            # 'name': 'Test S3 Write',
            "container": "testdata",
            "secrets": {"name": "Azure Blob", "type": "yamlconfigreader"},
        }

        self._writer = AzureBlobCSVWriter(**test_config)

    def tearDown(self) -> None:
        del self._writer

    def test_cotr(self):
        self.assertIsInstance(self._writer, DataframeWriter)
        self.assertEqual(self._writer._container, "testdata")

    def test_secrets(self):
        self.assertIsNotNone(self._writer._secrets.key)
        self.assertIsNotNone(self._writer._secrets.connection_string)

    def test_write(self):
        test_file = os.path.join("test_data", "test.csv")
        df = pd.read_csv(test_file)
        self._writer.execute(df=df, filename="test_file/2")
