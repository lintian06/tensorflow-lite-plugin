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

module lite {
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

  export function pluginRoute(pluginName: string, endPoint: string): string {
    // bug: /data/plugin/lite/data/plugin/lite/list_supported_ops not found, sending 404.
    // tf_backend.getRouter().pluginRoute(pluginName, endPoint); 
    const url = `/data/plugin/${pluginName}${endPoint}`;
    console.log('url: ' + url);
    return url;
  }

  export function graphUrl(run: string): string {
    const params = new URLSearchParams();
    params.set('run', run);
    params.set('conceptual', String(false));
    // if (tag) params.set('tag', tag);

    // const data = Object.keys(params).map(k => `${encodeURIComponent(k)}=${encodeURIComponent(params[k])}`);
    // const query = data.join('&');
    const url = `/data/plugin/graphs/graph?${params.toString()}`;
    //tf_backend.getRouter().pluginRoute(
    //    'graphs',
    //    '/graph',
    //    new URLSearchParams(query)
    //);
    console.log('url: ' + url);
    return url;
  }
}
