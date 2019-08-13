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
"""Use bazel to build."""
from __future__ import print_function

import common
import os
import setuptools
import shutil
import sys


os.chdir(common.ROOT_DIR)  # Change dir to the root folder.

_BUNLDE = common.BUNLDE
_LITE_DASHBOARD = "lite_dashboard"
_BAZEL_BIN = "bazel-bin"
_BAZEL_PY_OUT = os.path.join("bazel-out/k8-py3-fastbuild/bin", PLUGIN)

# To disable errors from com_google_protobuf/protobuf.bzl in bazel.
_PB_NO_CHECKS = [
    "--incompatible_disable_deprecated_attr_params=false",
    "--incompatible_new_actions_api=false",
    "--incompatible_depset_is_not_iterable=false",
    "--incompatible_no_support_tools_in_action_inputs=false",
]

def bazel_build(should_test=False):
  """Build sources with bazel."""
  print("--- Begin bazel ---")
  cmd = ["bazel build ..."]  # Build whole package.
  cmd += _PB_NO_CHECKS
  if should_test:
    cmd += ["&& bazel test ...:all"] + _PB_NO_CHECKS  # Test the package.
  cmd = " ".join(cmd)
  succeed = os.system(cmd) == 0
  print("--- End bazel: succeed=%s---" % succeed)
  return succeed


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
    plugin_out = os.path.join(_BUNDLE, PLUGIN)
    ignore = ["BUILD", _LITE_DASHBOARD]
    if ignore_test:
      ignore += ["*_test.py"]
    print("Copy tree %s to %s with some ignored." % (PLUGIN, plugin_out))
    shutil.copytree(PLUGIN, plugin_out, ignore=shutil.ignore_patterns(*ignore))

    # Prepare compiled html folder and files.
    os.makedirs(os.path.join(_BUNDLE, PLUGIN, _LITE_DASHBOARD))

    copy_pairs = [
        # index.html
        (
            os.path.join(_BAZEL_BIN, PLUGIN, _LITE_DASHBOARD, "index.html"),
            os.path.join(_BUNDLE, PLUGIN, _LITE_DASHBOARD, "index.html"),
        ),
        # index.js
        (
            os.path.join(PLUGIN, _LITE_DASHBOARD, "index.js"),
            os.path.join(_BUNDLE, PLUGIN, _LITE_DASHBOARD, "index.js"),
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


def main():
  if not bazel_build(should_test=True):
    sys.exit(common.BUILD_ERROR)

  if not prepare_bundle_folder(ignore_test=False):
    sys.exit(common.BUILD_ERROR)


if __name__ == '__main__':
  main()