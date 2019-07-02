# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""lite runner (called in subprocess).

This file builds a binary with libraries: tensorflow and numpy.
"""

import sys

from absl import app
import numpy as np   # pylint: disable=unused-import
import tensorflow as tf  # pylint: disable=unused-import


def run(script):
  """Run scripts in local environment."""
  exec(script)  # pylint: disable=exec-used


def main(_):
  input_script = sys.stdin.read()  # Readlines until EOF.
  run(input_script)


if __name__ == "__main__":
  app.run(main)
