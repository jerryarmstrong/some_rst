build-ts/index.browser.js
=========================

Last edited: 2020-08-26 04:48:13

Contents:

.. code-block:: js

    "use strict";
import WebSocketBrowserImpl from "./lib/client/websocket.browser";
import CommonClient from "./lib/client";
export class Client extends CommonClient {
    constructor(address = "ws://localhost:8080", { autoconnect = true, reconnect = true, reconnect_interval = 1000, max_reconnects = 5 } = {}, generate_request_id) {
        super(WebSocketBrowserImpl, address, {
            autoconnect,
            reconnect,
            reconnect_interval,
            max_reconnects
        }, generate_request_id);
    }
}


