build-ts/lib/client/websocket.js
================================

Last edited: 2020-08-26 04:48:13

Contents:

.. code-block:: js

    /* A wrapper for the "qaap/uws-bindings" library. */
"use strict";
import WebSocket from "ws";
/**
 * factory method for common WebSocket instance
 * @method
 * @param {String} address - url to a websocket server
 * @param {(Object)} options - websocket options
 * @return {Undefined}
 */
export default function (address, options) {
    return new WebSocket(address, options);
}


