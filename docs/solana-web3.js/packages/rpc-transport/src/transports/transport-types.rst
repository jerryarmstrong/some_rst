packages/rpc-transport/src/transports/transport-types.ts
========================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    type RpcTransportConfig = Readonly<{
    payload: unknown;
    signal?: AbortSignal;
}>;

export interface IRpcTransport {
    <TResponse>(config: RpcTransportConfig): Promise<TResponse>;
}


