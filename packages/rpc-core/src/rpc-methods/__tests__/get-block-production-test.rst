packages/rpc-core/src/rpc-methods/__tests__/get-block-production-test.ts
========================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';
import { createHttpTransport, createJsonRpc } from '@solana/rpc-transport';
import type { SolanaJsonRpcErrorCode } from '@solana/rpc-transport/dist/types/json-rpc-errors';
import type { Rpc } from '@solana/rpc-transport/dist/types/json-rpc-types';
import fetchMock from 'jest-fetch-mock-fork';

import { Commitment } from '../common';
import { createSolanaRpcApi, SolanaRpcMethods } from '../index';

describe('getBlockProduction', () => {
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
            it('returns block production data', async () => {
                expect.assertions(1);
                const blockProductionPromise = rpc.getBlockProduction({ commitment }).send();
                await expect(blockProductionPromise).resolves.toMatchObject({
                    value: expect.objectContaining({
                        byIdentity: expect.any(Object),
                        range: expect.objectContaining({
                            firstSlot: expect.any(BigInt),
                            lastSlot: expect.any(BigInt),
                        }),
                    }),
                });
            });

            it('has the latest context slot as the last slot', async () => {
                expect.assertions(1);
                const blockProduction = await rpc.getBlockProduction({ commitment }).send();
                expect(blockProduction.value.range.lastSlot).toBe(blockProduction.context.slot);
            });
        });
    });

    describe('when called with a single identity', () => {
        // Currently this call always returns just one identity in tests, so no way to meaningfully test this
        it.todo('returns data for just that identity');

        it('returns an empty byIdentity if the identity is not a block producer', async () => {
            expect.assertions(1);
            // Randomly generated address, assumed not to be a block producer
            const identity =
                '9NmqDDZa7mH1DBM4zeq9cm7VcRn2un1i2TwuMvjBoVhU' as Base58EncodedAddress<'9NmqDDZa7mH1DBM4zeq9cm7VcRn2un1i2TwuMvjBoVhU'>;
            const blockProductionPromise = rpc.getBlockProduction({ identity }).send();
            await expect(blockProductionPromise).resolves.toMatchObject({
                value: expect.objectContaining({
                    byIdentity: {},
                }),
            });
        });
    });

    describe('when called with a `lastSlot` higher than the highest slot available', () => {
        it('throws an error', async () => {
            expect.assertions(1);
            const blockProductionPromise = rpc
                .getBlockProduction({
                    range: {
                        firstSlot: 0n,
                        lastSlot: 2n ** 63n - 1n, // u64:MAX; safe bet it'll be too high.
                    },
                })
                .send();
            await expect(blockProductionPromise).rejects.toMatchObject({
                code: -32602 satisfies (typeof SolanaJsonRpcErrorCode)['JSON_RPC_INVALID_PARAMS'],
                message: expect.any(String),
                name: 'SolanaJsonRpcError',
            });
        });
    });
});


