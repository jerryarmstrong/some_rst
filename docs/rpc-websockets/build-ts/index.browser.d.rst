build-ts/index.browser.d.ts
===========================

Last edited: 2020-08-26 04:48:13

Contents:

.. code-block:: ts

    import CommonClient from "./lib/client";
import { IWSClientAdditionalOptions } from "./lib/client/client.types";
export declare class Client extends CommonClient {
    constructor(address?: string, { autoconnect, reconnect, reconnect_interval, max_reconnects }?: IWSClientAdditionalOptions, generate_request_id?: (method: string, params: object | Array<any>) => number);
}


