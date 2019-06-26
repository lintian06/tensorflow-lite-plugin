#!/bin/sh

set -e  # Exit if error.


DIR=`dirname "$0"`

echo "Now building pip..."
python $DIR/setup.py bdist_wheel --python-tag py2

# optional
echo "Now install..."
pip install $DIR/dist/tensorboard_lite_plugin-0.0.1-py2-none-any.whl -U
