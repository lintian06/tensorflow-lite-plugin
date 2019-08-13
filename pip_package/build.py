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
import sys
import os

import common


def main(args):
  if args.mode == "uninstall":
    cmd = "pip uninstall {plugin}".format(plugin=common.PLUGIN)
    common.run_success(cmd)

  elif args.mode == "install":
    # Bazel build.
    cmd = [
        "python {pip_dir}/bazel_build.py".format(pip_dir=common.PIP_DIR),
    ]
    print("Now building binary from source....")
    common.run_success(cmd)

    # Setup pip package.
    cmd = [
        "python {pip_dir}/setup.py".format(pip_dir=common.PIP_DIR),
        "build -b {build_dir}".format(build_dir=common.BUILD_DIR),
        "bdist_wheel",
        "--python-tag {python_tag}".format(python_tag=args.python_tag),
    ]
    print("Now building pip...")
    common.run_success(cmd)

    # Pip install.
    cmd = [
        "pip install",
        "{root_dir}/dist/{plugin}-{version}-{python_tag}-none-any.whl".format(
            root_dir=common.ROOT_DIR,
            plugin=common.PLUGIN,
            version=common.VERSION,
            python_tag=args.python_tag),
        "-U",
    ]
    print("Now install...")
    common.run_success(cmd)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Build tool.")
  parser.add_argument("--python_tag", type=str, default="py3",
                      help="Python version. Valid: py2 or py3")
  parser.add_argument("--mode", type=str, default="install",
                      help="Mode. Valid: install or uninstall")
  main(parser.parse_args())
