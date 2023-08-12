packages/rpc-core/src/rpc-methods/__tests__/is-blockhash-valid-test.ts
======================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { createHttpTransport, createJsonRpc } from '@solana/rpc-transport';
import type { Rpc } from '@solana/rpc-transport/dist/types/json-rpc-types';
import { Blockhash } from '@solana/transactions';
import fetchMock from 'jest-fetch-mock-fork';

import { Commitment } from '../common';
import { createSolanaRpcApi, SolanaRpcMethods } from '../index';

describe('isBlockhashValid', () => {
    let rpc: Rpc<SolanaRpcMethods>;
    beforeEach(() => {
        fetchMock.resetMocks();
        fetchMock.dontMock();
        rpc = createJsonRpc<SolanaRpcMethods>({
            api: createSolanaRpcApi(),
            transport: createHttpTransport({ url: 'http://127.0.0.1:8899' }),
        });
    });
    (['confirmed', 'finalized', 'processed'] as Commitment[]).forEach(commitment => {
        describe(`when called with \`${commitment}\` commitment`, () => {
            it('returns the result as a bool wrapped in an RpcResponse', async () => {
                expect.assertions(1);
                const blockhash = '9PCVWkKP3bq1sT5eLFurUysMvVs4PxJsTfza5QSBB4d1' as Blockhash;
                const result = await rpc.isBlockhashValid(blockhash, { commitment }).send();
                expect(result.value).toEqual(expect.any(Boolean));
            });
        });
    });
});


