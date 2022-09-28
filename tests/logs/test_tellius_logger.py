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
import logging
from unittest import TestCase

from tellius_data_manager.logs.tellius_logger import TelliusLogger


class TestTelliusLogger(TestCase):
    def setUp(self) -> None:
        class LogTest:
            def __init__(self):
                logging.setLoggerClass(TelliusLogger)
                self._logger = logging.getLogger(__name__)

            def log(self, msg):
                self._logger.info(msg)

        self._class = LogTest()

    def tearDown(self) -> None:
        pass

    def test_log_info(self):
        self._class.log("test message")
