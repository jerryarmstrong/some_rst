packages/rpc-core/src/rpc-methods/__tests__/get-cluster-nodes-test.ts
=====================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { createHttpTransport, createJsonRpc } from '@solana/rpc-transport';
import type { Rpc } from '@solana/rpc-transport/dist/types/json-rpc-types';
import fetchMock from 'jest-fetch-mock-fork';

import { createSolanaRpcApi, SolanaRpcMethods } from '../index';

describe('getClusterNodes', () => {
    let rpc: Rpc<SolanaRpcMethods>;
    beforeEach(() => {
        fetchMock.resetMocks();
        fetchMock.dontMock();
        rpc = createJsonRpc<SolanaRpcMethods>({
            api: createSolanaRpcApi(),
            transport: createHttpTransport({ url: 'http://127.0.0.1:8899' }),
        });
    });

    describe('when run against the test validator', () => {
        it('returns RPC and validator info', async () => {
            expect.assertions(1);
            const res = await rpc.getClusterNodes().send();
            expect(res).toEqual(
                expect.arrayContaining([
                    expect.objectContaining({
                        gossip: expect.any(String),
                        rpc: expect.any(String),
                        tpu: expect.any(String),
                    }),
                ])
            );
        });
    });
});


