# The TensorFlow Lite Dashboard

This dashboard displays TensorFlow Lite compatibility in graph explorer,
developers are able to visually explore the graph and know ops compatibility.
It makes their life easier to convert a TF graph to TFLite, when specifying the
inputs and outputs.

![The TensorFlow Lite Dashboard](tensorboard_lite_plugin/images/lite_intro.png)

Features:
  * Identify supported and unsupported ops with colors.
  * Calculate the coverage of compatible ops.
  * List incompatible operations. Click on an operation to zoom in on the
    selected op.
  * Select nodes and convert TensorFlow model into TF Lite.


## Installation:
*Prerequisite*:

[bazel](https://docs.bazel.build/versions/master/install-ubuntu.html) >=0.24.1.

### How to install the plugin of developer preview version.
```
# Clone this repo.
git clone https://github.com/lintian06/tensorflow-lite-plugin
# Build and install tensorflow-lite-plugin.
sh tensorflow-lite-plugin/build.sh

# Optional: Generate demo folder to /tmp/lite-demo
python -m tensorboard_lite_plugin.lite_demo
```

### Run TensorBoard
Run the latest TensorBoard.
```
tensorboard --logdir=/tmp/lite-demo   # Or other model folder of your own.
```
You will see a prompted URL. Open the link with your web browser.

### Develop the Plugin with TensorBoard Dev Version.

```
# Clone tensorboard with specific development snapshot.
git clone https://github.com/lintian06/tensorboard -b lite_plugin_fix_dep2
cd tensorboard
bazel run //tensorboard -- --logdir=/tmp/lite-demo
```
