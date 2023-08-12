src/index.ts
============

Last edited: 2020-08-26 04:48:13

Contents:

.. code-block:: ts

    "use strict"

import WebSocket from "./lib/client/websocket"
import CommonClient from "./lib/client"
import { NodeWebSocketTypeOptions, IWSClientAdditionalOptions } from "./lib/client/client.types"

export class Client extends CommonClient
{
    constructor(
        address = "ws://localhost:8080",
        {
            autoconnect = true,
            reconnect = true,
            reconnect_interval = 1000,
            max_reconnects = 5,
            ...rest_options
        }: IWSClientAdditionalOptions & NodeWebSocketTypeOptions = {},
        generate_request_id?: (method: string, params: object | Array<any>) => number
    )
    {
        super(
            WebSocket,
            address,
            {
                autoconnect,
                reconnect,
                reconnect_interval,
                max_reconnects,
                ...rest_options
            },
            generate_request_id
        )
    }
}

export {default as Server} from "./lib/server"


