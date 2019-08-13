#!/bin/bash
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
from __future__ import print_function

import argparse
import common
import sys
import os


def assert_success(cmd):
  """Runns cmd, and assert succeed."""
  print("Run: {}".format(cmd))
  if os.system(cmd) != 0:
    print("Failed with: {}".format(cmd))
    sys.exit(common.BUILD_ERROR)


def main(args):
  if args.mode == "uninstall":
    cmd = "pip uninstall {plugin}".format(plugin=common.PLUGIN)
    assert_success(cmd)

  elif args.mode == "install":
    # Setup pip package.
    cmd = "python {pip_dir}/setup.py bdist_wheel --python-tag {python_tag}".format(
      pip_dir=common.PIP_DIR, python_tag=args.python_tag)
    
    print("Now building pip...")
    assert_success(cmd)

    # Pip install.
    cmd = "pip install {root_dir}/dist/{plugin}-{version}-{python_tag}-none-any.whl -U".format(
      root_dir=common.ROOT_DIR, plugin=common.PLUGIN, version=common.VERSION, python_tag=args.python_tag)
    
    print("Now install...")
    assert_success(cmd)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Build tool.")
  parser.add_argument("--python_tag", type=str, default="py3",
                      help="Python version. Valid: py2 or py3")
  parser.add_argument("--mode", type=str, default="install",
                      help="Mode. Valid: install or uninstall")

  args = parser.parse_args()
  main(args)
