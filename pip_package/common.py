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
"""Common constants for setup."""

import os

BUILD_ERROR = -1  # Error code

PIP_DIR = os.path.abspath(os.path.dirname(__file__))  # pip_package folder.
ROOT_DIR = os.path.dirname(PIP_DIR)  # Root folder.
BUNDLE = "_bundle_srcs"  # Build target for bundle folder.

PLUGIN = "tensorboard_lite_plugin"  # Plugin subfolder under root.

PLUGIN_NAME = "tensorboard-lite-plugin"  # Plugin name.
VERSION = "0.1.0"
