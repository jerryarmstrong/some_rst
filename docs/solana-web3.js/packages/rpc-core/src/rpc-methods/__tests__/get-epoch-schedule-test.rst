packages/rpc-core/src/rpc-methods/__tests__/get-epoch-schedule-test.ts
======================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { createHttpTransport, createJsonRpc } from '@solana/rpc-transport';
import type { Rpc } from '@solana/rpc-transport/dist/types/json-rpc-types';
import fetchMock from 'jest-fetch-mock-fork';

import { createSolanaRpcApi, SolanaRpcMethods } from '../index';

describe('getEpochSchedule', () => {
    let rpc: Rpc<SolanaRpcMethods>;
    beforeEach(() => {
        fetchMock.resetMocks();
        fetchMock.dontMock();
        rpc = createJsonRpc<SolanaRpcMethods>({
            api: createSolanaRpcApi(),
            transport: createHttpTransport({ url: 'http://127.0.0.1:8899' }),
        });
    });

    it('returns the epoch schedule', async () => {
        expect.assertions(1);
        const epochSchedulePromise = rpc.getEpochSchedule().send();
        await expect(epochSchedulePromise).resolves.toMatchObject({
            firstNormalEpoch: expect.any(BigInt),
            firstNormalSlot: expect.any(BigInt),
            leaderScheduleSlotOffset: expect.any(BigInt),
            slotsPerEpoch: expect.any(BigInt),
            warmup: expect.any(Boolean),
        });
    });
});


