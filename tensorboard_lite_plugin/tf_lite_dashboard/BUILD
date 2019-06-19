# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
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

package(default_visibility = ["@org_tensorflow_tensorboard//tensorboard:internal"])

load("@org_tensorflow_tensorboard//tensorboard/defs:web.bzl", "tf_web_library")

licenses(["notice"])  # Apache 2.0


tf_web_library(
    name = "tf_lite_common",
    srcs = [
        "op.ts",
        "tf-lite-common.html",
    ],
    path = "/tf-lite-common",
    deps = [
        "@org_tensorflow_tensorboard//tensorboard/plugins/graph/tf_graph_common",
    ],
)

tf_web_library(
    name = "tf_lite_controls",
    srcs = ["tf-lite-controls.html"],
    path = "/tf-lite-controls",
    deps = [
        "//tensorboard_lite_plugin/tf_lite_common",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_imports:polymer",
        "@org_polymer_iron_pages",
        "@org_polymer_paper_button",
        "@org_polymer_paper_icon_button",
        "@org_polymer_paper_dialog",
        "@org_polymer_paper_toast",
        "@org_polymer_paper_item",
        "@org_polymer_paper_listbox",
        "@org_polymer_paper_radio_group",
        "@org_polymer_paper_tooltip",
        "@org_polymer_paper_tabs"
    ],
)

tf_web_library(
    name = "tf_lite_dashboard",
    srcs = [
        "tf-lite-dashboard.html",
    ],
    path = "/tf-lite-dashboard",
    deps = [
        ":tf_lite_common",
        ":tf_lite_controls",
        "//tensorboard/components/tf_backend",
        "//tensorboard/components/tf_dashboard_common",
        "//tensorboard/components/tf_imports:polymer",
        "//tensorboard/components/tf_tensorboard:registry",
        "//tensorboard/components/tf_imports:webcomponentsjs",
        "//tensorboard/plugins/graph/tf_graph_board",
        "//tensorboard/plugins/graph/tf_graph_loader",
    ],
)
