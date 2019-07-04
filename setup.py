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
from __future__ import print_function

import os
import shutil
import sys
import setuptools


_BUILD_ERROR = -1  # Error code
_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
os.chdir(_BASE_DIR)  # Change dir to the parent folder.

_BUNDLE = "_bundle_srcs"
_PLUGIN = "tensorboard_lite_plugin"
_LITE_DASHBOARD = "lite_dashboard"
_BAZEL_BIN = "bazel-bin"
_BAZEL_PY_OUT = os.path.join("bazel-out/k8-py3-fastbuild/bin", _PLUGIN)


def bazel_build(should_test=False):
  """Build sources with bazel."""
  print("--- Begin bazel ---")
  cmd = "bazel build ..."  # Build whole package.
  if should_test:
    cmd = cmd + " && bazel test ...:all"  # Test the package.
  succeed = os.system(cmd) == 0
  print("--- End bazel: succeed=%s---" % succeed)
  return succeed

if not bazel_build(should_test=False):
  sys.exit(_BUILD_ERROR)


def prepare_bundle_folder(ignore_test):
  """Prepare package code inside `_BUNDLE` folder."""
  print("Prepare bundled package folder: %s..." % _BUNDLE)
  print("--- Begin ---")

  succeed = False
  try:
    # Prepare a brand new folder.
    if os.path.exists(_BUNDLE):
      shutil.rmtree(_BUNDLE)
    os.makedirs(_BUNDLE)

    # Prepare py files.
    plugin_out = os.path.join(_BUNDLE, _PLUGIN)
    ignore = ["BUILD", _LITE_DASHBOARD]
    if ignore_test:
      ignore += ["*_test.py"]
    print("Copy tree %s to %s with some ignored." % (_PLUGIN, plugin_out))
    shutil.copytree(_PLUGIN, plugin_out, ignore=shutil.ignore_patterns(*ignore))

    # Prepare compiled html folder and files.
    os.makedirs(os.path.join(_BUNDLE, _PLUGIN, _LITE_DASHBOARD))

    copy_pairs = [
        # index.html
        (
            os.path.join(_BAZEL_BIN, _PLUGIN, _LITE_DASHBOARD, "index.html"),
            os.path.join(_BUNDLE, _PLUGIN, _LITE_DASHBOARD, "index.html"),
        ),
        # index.js
        (
            os.path.join(_PLUGIN, _LITE_DASHBOARD, "index.js"),
            os.path.join(_BUNDLE, _PLUGIN, _LITE_DASHBOARD, "index.js"),
        ),
    ]
    for file_in, file_out in copy_pairs:
      print("Copy: %s to %s" % (file_in, file_out))
      shutil.copy2(file_in, file_out)

    print("--- End ---")
    succeed = True
  except Exception as e:  # pylint: disable=broad-except
    print(e)
  return succeed

if not prepare_bundle_folder(ignore_test=False):
  sys.exit(_BUILD_ERROR)


with open("README.md", "r") as fh:
  long_description = fh.read()

REQUIRED_PACKAGES = [
    "werkzeug >= 0.11.15",
    "tensorboard >= 1.13.0",
    "tensorflow >= 1.14.0",
]

setuptools.setup(
    name="tensorboard-lite-plugin",
    version="0.1.0",
    author="TensorFlow Lite team",
    author_email="tflite@tensorflow.org",
    description="TF Lite Plugin for TensorBoard.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tensorflow/tensorboard_lite_plugin",
    packages=setuptools.find_packages(where=_BUNDLE),
    package_dir={"": _BUNDLE},
    entry_points={
        "tensorboard_plugins": [
            "lite=tensorboard_lite_plugin.lite_plugin:LitePlugin",
        ],
    },
    package_data={
        # Must keep this in sync with assets files.
        "tensorboard_lite_plugin": ["lite_dashboard/index.html",],
    },
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
