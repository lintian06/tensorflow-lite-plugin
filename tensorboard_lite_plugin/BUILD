# Description:
# TensorBoard plugin for TF Lite.
package(default_visibility = [":internal"])

licenses(["notice"])  # Apache 2.0

package_group(
    name = "internal",
    packages = ["//tensorboard_lite_plugin/..."],
)

py_library(
    name = "lite_backend",
    srcs = ["lite_backend.py"],
    srcs_version = "PY2AND3",
    deps = [
        "@org_pythonhosted_six",
        "@org_tensorflow_tensorboard//tensorboard:expect_tensorflow_installed",
    ],
)

py_library(
    name = "lite_plugin",
    srcs = ["lite_plugin.py"],
    data = [
        "//tensorboard_lite_plugin/lite_dashboard:assets",
    ],
    srcs_version = "PY2AND3",
    deps = [
        ":lite_backend",
        "@org_pocoo_werkzeug",
        "@org_tensorflow_tensorboard//tensorboard:plugin_util",
        "@org_tensorflow_tensorboard//tensorboard/backend:http_util",
        "@org_tensorflow_tensorboard//tensorboard/backend/event_processing:event_accumulator",
        "@org_tensorflow_tensorboard//tensorboard/plugins:base_plugin",
    ],
)

py_library(
    name = "lite_plugin_loader",
    srcs = ["lite_plugin_loader.py"],
    srcs_version = "PY2AND3",
    deps = [
        ":lite_backend",
        ":lite_plugin",
        "@org_tensorflow_tensorboard//tensorboard/plugins:base_plugin",
    ],
)

py_test(
    name = "lite_backend_test",
    size = "medium",  # tf integration test
    srcs = ["lite_backend_test.py"],
    python_version = "PY3",
    srcs_version = "PY2AND3",
    deps = [
        ":lite_backend",
        ":lite_demo_model",
        "@org_tensorflow_tensorboard//tensorboard:expect_tensorflow_installed",
    ],
)

py_test(
    name = "lite_plugin_test",
    size = "medium",  # tf integration test
    srcs = ["lite_plugin_test.py"],
    python_version = "PY3",
    srcs_version = "PY2AND3",
    deps = [
        ":lite_backend",
        ":lite_demo_model",
        ":lite_plugin",
        ":lite_plugin_loader",
        "@org_pocoo_werkzeug",
        "@org_tensorflow_tensorboard//tensorboard:expect_tensorflow_installed",
        "@org_tensorflow_tensorboard//tensorboard/backend:application",
        "@org_tensorflow_tensorboard//tensorboard/plugins:base_plugin",
    ],
)

py_test(
    name = "lite_plugin_loader_test",
    size = "small",  # tf integration test
    srcs = ["lite_plugin_loader_test.py"],
    python_version = "PY3",
    srcs_version = "PY2AND3",
    deps = [
        ":lite_backend",
        ":lite_plugin",
        ":lite_plugin_loader",
        "@org_tensorflow_tensorboard//tensorboard:expect_tensorflow_installed",
        "@org_tensorflow_tensorboard//tensorboard/backend:application",
        "@org_tensorflow_tensorboard//tensorboard/plugins:base_plugin",
    ],
)

py_binary(
    name = "lite_demo",
    srcs = ["lite_demo.py"],
    python_version = "PY3",
    srcs_version = "PY2AND3",
    deps = [
        ":lite_demo_model",
        "@org_tensorflow_tensorboard//tensorboard:expect_absl_app_installed",
        "@org_tensorflow_tensorboard//tensorboard:expect_absl_flags_installed",
        "@org_tensorflow_tensorboard//tensorboard:expect_tensorflow_installed",
    ],
)

py_library(
    name = "lite_demo_model",
    srcs = ["lite_demo_model.py"],
    srcs_version = "PY2AND3",
    deps = [
        "@org_tensorflow_tensorboard//tensorboard:expect_numpy_installed",
        "@org_tensorflow_tensorboard//tensorboard:expect_tensorflow_installed",
    ],
)
