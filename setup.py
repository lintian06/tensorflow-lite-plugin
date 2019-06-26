import os
import setuptools
import shutil
import sys
import glob


_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
os.chdir(_BASE_DIR)

_BUNDLE = '_bundle_srcs'
_PLUGIN = 'tensorboard_lite_plugin'
_DASHBOARD = 'lite_dashboard'
_BAZEL_BIN = 'bazel-bin'
_INDEX_HTML = 'index.html'
_INDEX_JS = 'index.js'


def bazel_build():
  """Build sources with bazel."""
  print('Bazel build...')
  print('--- Begin ---')
  succeed = os.system("bazel build //tensorboard_lite_plugin/...") == 0
  print('--- End ---')
  return succeed

if not bazel_build():
  sys.exit()


def prepare_bundle_folder(ignore_test):
  """Prepare package code inside `_BUNDLE` folder."""
  print('Prepare bundled package folder: %s...' % _BUNDLE)
  print('--- Begin ---')

  succeed = False
  try:
    # Prepare a brand new folder.
    if os.path.exists(_BUNDLE):
      shutil.rmtree(_BUNDLE)
    os.makedirs(_BUNDLE)
    
    # Prepare py files.
    plugin_out = os.path.join(_BUNDLE, _PLUGIN)
    ignore = ['BUILD', _DASHBOARD]
    if ignore_test:
      ignore += ['*_test.py']
    print('Copy tree %s to %s with some ignored.' % (_PLUGIN, plugin_out))
    shutil.copytree(_PLUGIN, plugin_out, ignore=shutil.ignore_patterns(*ignore))
    
    # Prepare compiled html files.
    os.makedirs(os.path.join(_BUNDLE, _PLUGIN, _DASHBOARD))
    index_html_in = os.path.join(_BAZEL_BIN, _PLUGIN, _DASHBOARD, _INDEX_HTML)
    index_html_out = os.path.join(_BUNDLE, _PLUGIN, _DASHBOARD, _INDEX_HTML)
    print('Copy: %s to %s' % (index_html_in, index_html_out))
    shutil.copy2(index_html_in, index_html_out)

    index_js_in = os.path.join(_PLUGIN, _DASHBOARD, _INDEX_JS)
    index_js_out = os.path.join(_BUNDLE, _PLUGIN, _DASHBOARD, _INDEX_JS)
    print('Copy: %s to %s' % (index_js_in, index_js_out))
    shutil.copy2(index_js_in, index_js_out)
    print('--- End ---')
    succeed = True
  except e:
    print(e)
  finally:
    return succeed

if not prepare_bundle_folder(ignore_test=True):
  sys.exit()


with open("README.md", "r") as fh:
  long_description = fh.read()

REQUIRED_PACKAGES = [
  'werkzeug >= 0.11.15',
  'tensorboard >= 1.13.0',
]

setuptools.setup(
  name="tensorboard-lite-plugin",
  version="0.0.1",
  author="TensorFlow Lite team",
  author_email="tflite@tensorflow.org",
  description="TF Lite Plugin for TensorBoard.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/tensorflow/tensorboard_lite_plugin",
  packages=setuptools.find_packages(where=_BUNDLE),
  package_dir={'': _BUNDLE},
  entry_points={
    "tensorboard_plugins": [
      "lite=tensorboard_lite_plugin.lite_plugin:LitePlugin",
    ],
  },
  package_data={
    # Must keep this in sync with tf_projector_plugin:projector_assets
    'tensorboard_lite_plugin': [
        'lite_dashboard/index.html',
    ],
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