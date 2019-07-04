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

package(default_visibility = ["//tensorboard_lite_plugin:internal"])

load("@org_tensorflow_tensorboard//tensorboard/defs:web.bzl", "tf_web_library")
load("@org_tensorflow_tensorboard//tensorboard/defs:vulcanize.bzl", "tensorboard_html_binary")

tf_web_library(
    name = "lite_common",
    srcs = [
        "common.js",
        "lite-common.html",
    ],
    path = "/lite-common",
    deps = [
        "@org_tensorflow_tensorboard//tensorboard/components/tf_backend",
        "@org_tensorflow_tensorboard//tensorboard/plugins/graph/tf_graph_common",
    ],
)

tf_web_library(
    name = "lite_controls",
    srcs = [
        "lite-controls.html",
    ],
    path = "/lite-controls",
    deps = [
        ":lite_common",
        "@org_polymer_iron_icon",
        "@org_polymer_iron_icons",
        "@org_polymer_iron_pages",
        "@org_polymer_paper_button",
        "@org_polymer_paper_dialog",
        "@org_polymer_paper_dropdown_menu",
        "@org_polymer_paper_icon_button",
        "@org_polymer_paper_item",
        "@org_polymer_paper_listbox",
        "@org_polymer_paper_menu",
        "@org_polymer_paper_radio_group",
        "@org_polymer_paper_tabs",
        "@org_polymer_paper_toast",
        "@org_polymer_paper_tooltip",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_dashboard_common",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_imports:polymer",
        "@org_tensorflow_tensorboard//tensorboard/plugins/graph/tf_graph_node_search",
    ],
)

tf_web_library(
    name = "lite_dashboard",
    srcs = [
        "lite-dashboard.html",
    ],
    path = "/lite-dashboard",
    deps = [
        ":lite_common",
        ":lite_controls",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_backend",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_dashboard_common",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_imports:polymer",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_storage",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_tensorboard:registry",
        "@org_tensorflow_tensorboard//tensorboard/plugins/graph/tf_graph_board",
        "@org_tensorflow_tensorboard//tensorboard/plugins/graph/tf_graph_loader:tf_graph_dashboard_loader",
    ],
)

tf_web_library(
    name = "index_tpl",
    srcs = ["index-tpl.html"],
    path = "/lite-index-tpl",
    deps = [
        ":lite_dashboard",
        "@org_polymer_paper_button",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_imports:webcomponentsjs",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_tensorboard",
    ],
)

tensorboard_html_binary(
    name = "index",
    compile = True,
    input_path = "/lite-index-tpl/index-tpl.html",
    output_path = "/lite-tensorboard/index.html",
    deps = [
        ":index_tpl",
    ],
)

tf_web_library(
    name = "assets",
    srcs = [
        "index.html",
        "index.js",
    ],
    path = "/lite-dashboard",
    deps = [
        ":lite_dashboard",
        "@org_tensorflow_tensorboard//tensorboard/components/tf_imports:webcomponentsjs",
    ],
)
