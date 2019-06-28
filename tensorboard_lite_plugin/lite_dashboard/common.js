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
var lite;
(function (lite) {
  // A class implements tf.graph.op.CompatibilityProvider.
  var LiteCompatibilityProvider = /** @class */ (function () {
    function LiteCompatibilityProvider(whitelist) {
    	this._whitelist = whitelist;  // string[]
    }
    /**
     * Checks whether a op node is valid.
     * @param tf.graph.OpNode
     * @return boolean
     */
    LiteCompatibilityProvider.prototype.opValid = function(opNode) {
      console.log('this._whitelist: ', this._whitelist);
      console.log('opNode: ', opNode);
      return this._whitelist && this._whitelist.indexOf(opNode.op) != -1;
    }

    return LiteCompatibilityProvider;
  })();
  lite.LiteCompatibilityProvider = LiteCompatibilityProvider;

  // Lite Plugin name.
  lite.PLUGIN = 'lite';
  // Lite Plugin name.
  lite.LIST_SUPPORTED_OPS = '/list_supported_ops';
  lite.LIST_SAVED_MODELS = '/list_saved_models';
  lite.SCRIPT = '/script';
  lite.CONVERT = '/convert';
  // Redirect for other plugins.
  lite.GRAPHS_PLUGIN = 'graphs';
  lite.GRAPHS_INFO = '/info';
  lite.GRAPHS_GRAPH = '/graph';

  // The original of dynamic plugin starts with path:
  //   http://hostname/data/plugin/lite
  // So For dynamic plugin, it uses the relative path as follows.
  var _router = tf_backend.createRouter("../../../data");

  /**
   * Gets router.
   * @return tf_backend.Router
   */
  function getRouter() {
    return _router;
  }
  lite.getRouter = getRouter;

  // Reset tf_backend.getRouter.
  // As the plugin uses separate <iframe>, it won't have side effect.
  tf_backend.getRouter = getRouter;
})(lite || (lite = {}));  // namespace tf_backend