packages/rpc-transport/src/json-rpc-message.ts
==============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { getNextMessageId } from './json-rpc-message-id';

export function createJsonRpcMessage<TParams>(method: string, params: TParams) {
    return {
        id: getNextMessageId(),
        jsonrpc: '2.0',
        method,
        params,
    };
}


