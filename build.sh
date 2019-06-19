echo "Now building pip"
python setup.py bdist_wheel --python-tag py2

# optional
# pip install dist/lite_tensorboard_plugin-0.0.1-py2-none-any.whl -U