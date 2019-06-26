/* Copyright 2017 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

namespace lite {

  import CompatibilityProvider = tf.graph.op.CompatibilityProvider;
  import OpNode = tf.graph.OpNode;

  export class LiteCompatibilityProvider implements CompatibilityProvider {
    private _whitelist: string[];

    constructor(whitelist: string[]) {
      this._whitelist = whitelist;
    }

    opValid(opNode: OpNode): boolean {
      return this._whitelist && this._whitelist.indexOf(opNode.op) != -1;
    }
  }

  // Lite Plugin name
  export const PLUGIN = 'lite';
  export const LIST_SUPPORTED_OPS = '/list_supported_ops';
  export const LIST_SAVED_MODELS = '/list_saved_models';
  export const SCRIPT = '/script';
  export const CONVERT = '/convert';
  // Redirect: 
  export const GRAPHS_PLUGIN = 'graphs';
  export const GRAPHS_INFO = '/info';
  export const GRAPHS_GRAPH = '/graph';

  // The original of dynamic plugin starts with path:
  //   http://hostname/data/plugin/lite
  // So For dynamic plugin, it uses the relative path as follows.
  const _router = tf_backend.createRouter("../../../data");
  // Reset tf_backend.getRouter. 
  // As the plugin uses separate <iframe>, it won't have side effect.
  tf_backend.getRouter = getRouter;

  export function getRouter(): tf_backend.Router {
    return _router;
  }
}  // namespace lite