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
from typing import Dict
from unittest import TestCase
from tellius_data_manager.pipes.logics.if_step import IfStep


class TestIf(TestCase):
    def setUp(self) -> None:
        self._pipe = IfStep(name="test_if")

    def tearDown(self) -> None:
        del self._pipe

    def test_run_no_inputs(self):
        def test_func() -> bool:
            return True

        output = self._pipe.run(if_test_function=test_func)

        self.assertTrue(output.info["if_truth"])

    def test_run_inputs_true(self):
        def test_func(value: float) -> bool:
            if value > 3:
                return True
            else:
                return False

        inputs = {"value": 4}
        output = self._pipe.run(inputs=inputs, if_test_function=test_func)

        self.assertTrue(output.info["if_truth"])

    def test_run_inputs_false(self):
        def test_func(value: float) -> bool:
            if value > 3:
                return True
            else:
                return False

        inputs = {"value": 2}
        output = self._pipe.run(inputs=inputs, if_test_function=test_func)

        self.assertFalse(output.info["if_truth"])

    def test_run_inputs_lambda(self):
        test_func = lambda: True

        output = self._pipe.run(if_test_function=test_func)
        self.assertTrue(output.info["if_truth"])
