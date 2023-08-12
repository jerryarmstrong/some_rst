src/index.browser.ts
====================

Last edited: 2020-08-26 04:48:13

Contents:

.. code-block:: ts

    "use strict"

import WebSocketBrowserImpl from "./lib/client/websocket.browser"
import CommonClient from "./lib/client"
import { IWSClientAdditionalOptions } from "./lib/client/client.types"

export class Client extends CommonClient
{
    constructor(
        address = "ws://localhost:8080",
        {
            autoconnect = true,
            reconnect = true,
            reconnect_interval = 1000,
            max_reconnects = 5
        }: IWSClientAdditionalOptions = {},
        generate_request_id?: (method: string, params: object | Array<any>) => number
    )
    {
        super(
            WebSocketBrowserImpl,
            address,
            {
                autoconnect,
                reconnect,
                reconnect_interval,
                max_reconnects
            },
            generate_request_id
        )
    }
}

