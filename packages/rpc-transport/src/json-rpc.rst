packages/rpc-transport/src/json-rpc.ts
======================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { SolanaJsonRpcError } from './json-rpc-errors';
import { createJsonRpcMessage } from './json-rpc-message';
import { PendingRpcRequest, Rpc, RpcConfig, RpcRequest, SendOptions } from './json-rpc-types';

interface IHasIdentifier {
    readonly id: number;
}
type JsonRpcResponse<TResponse> = IHasIdentifier &
    Readonly<{ result: TResponse } | { error: { code: number; message: string; data?: unknown } }>;

function createPendingRpcRequest<TRpcMethods, TResponse>(
    rpcConfig: RpcConfig<TRpcMethods>,
    pendingRequest: RpcRequest<TResponse>
): PendingRpcRequest<TResponse> {
    return {
        async send(options?: SendOptions): Promise<TResponse> {
            const { methodName, params, responseProcessor } = pendingRequest;
            const payload = createJsonRpcMessage(methodName, params);
            const response = await rpcConfig.transport<JsonRpcResponse<unknown>>({
                payload,
                signal: options?.abortSignal,
            });
            if ('error' in response) {
                throw new SolanaJsonRpcError(response.error);
            } else {
                return (responseProcessor ? responseProcessor(response.result) : response.result) as TResponse;
            }
        },
    };
}

function makeProxy<TRpcMethods>(rpcConfig: RpcConfig<TRpcMethods>): Rpc<TRpcMethods> {
    return new Proxy(rpcConfig.api, {
        defineProperty() {
            return false;
        },
        deleteProperty() {
            return false;
        },
        get(target, p, receiver) {
            return function (...rawParams: unknown[]) {
                const methodName = p.toString();
                const createRpcRequest = Reflect.get(target, methodName, receiver);
                const newRequest = createRpcRequest
                    ? createRpcRequest(...rawParams)
                    : { methodName, params: rawParams };
                return createPendingRpcRequest(rpcConfig, newRequest);
            };
        },
    }) as Rpc<TRpcMethods>;
}

export function createJsonRpc<TRpcMethods>(rpcConfig: RpcConfig<TRpcMethods>): Rpc<TRpcMethods> {
    return makeProxy(rpcConfig);
}


