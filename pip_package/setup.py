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
"""setup for pip package."""
import os

import common
import setuptools


os.chdir(common.ROOT_DIR)   # Change dir to the root folder.


with open("README.md", "r") as fh:
  long_description = fh.read()

with open("requirements.txt", "r") as fh:
  # Filter empty or comments.
  valid_package = lambda l: l and not l.startswith("#")
  required_packages = [l for l in fh.read().splitlines() if valid_package(l)]


setuptools.setup(
    name=common.PLUGIN_NAME,
    version=common.VERSION,
    author="TensorFlow Lite team",
    author_email="tflite@tensorflow.org",
    description="TF Lite Plugin for TensorBoard.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tensorflow/tensorboard_lite_plugin",
    packages=setuptools.find_packages(where=common.BUNDLE),
    package_dir={"": common.BUNDLE},
    entry_points={
        "tensorboard_plugins": [
            "lite=tensorboard_lite_plugin.lite_plugin:LitePlugin",
        ],
    },
    package_data={
        # Must keep this in sync with assets files.
        "tensorboard_lite_plugin": [
            "lite_dashboard/index.html",
            "lite_dashboard/index.js",
            "images/lite_intro.png",
        ],
    },
    include_package_data=True,
    install_requires=required_packages,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
