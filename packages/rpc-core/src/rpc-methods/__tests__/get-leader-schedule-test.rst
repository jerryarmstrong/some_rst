packages/rpc-core/src/rpc-methods/__tests__/get-leader-schedule-test.ts
=======================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { base58 } from '@metaplex-foundation/umi-serializers';
import { Base58EncodedAddress } from '@solana/addresses';
import { createHttpTransport, createJsonRpc } from '@solana/rpc-transport';
import type { Rpc } from '@solana/rpc-transport/dist/types/json-rpc-types';
import assert from 'assert';
import fetchMock from 'jest-fetch-mock-fork';

import validatorIdentityBytes from '../../../../../test-ledger/validator-keypair.json';
import { Commitment } from '../common';
import { createSolanaRpcApi, SolanaRpcMethods } from '../index';

function getValidatorAddress(): Base58EncodedAddress {
    const secretKey = new Uint8Array(validatorIdentityBytes);
    const publicKey = secretKey.slice(32, 64);
    const address = base58.deserialize(publicKey)[0];
    return address as Base58EncodedAddress;
}

describe('getLeaderSchedule', () => {
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
            describe('when called with no identity and no slot', () => {
                it('returns the leader schedule for all cluster nodes in the current epoch', async () => {
                    expect.assertions(3);
                    const res = await rpc.getLeaderSchedule({ commitment }).send();
                    // Does not need null check (default slot)
                    expect(res).toMatchObject(expect.any(Object));
                    for (const key of Object.keys(res)) {
                        expect(typeof key).toBe('string');
                        // Needs typecasting to be used as accessor
                        const base58Key: Base58EncodedAddress = key as Base58EncodedAddress;
                        expect(res[base58Key]).toMatchObject(expect.any(Array));
                    }
                });
            });

            describe('when called with no identity and a valid slot', () => {
                it('returns the leader schedule for all cluster nodes in the epoch corresponding to the provided slot', async () => {
                    expect.assertions(3);
                    const res = await rpc.getLeaderSchedule(0n, { commitment }).send();
                    // Needs null check (slot provided and may correspond to epoch that does not exist)
                    expect(res).toMatchObject(expect.any(Object));
                    assert(res);
                    for (const key of Object.keys(res)) {
                        expect(typeof key).toBe('string');
                        // Needs typecasting to be used as accessor
                        const base58Key: Base58EncodedAddress = key as Base58EncodedAddress;
                        expect(res[base58Key]).toMatchObject(expect.any(Array));
                    }
                });
            });

            describe('when called with an account that is a validator identity and no slot', () => {
                it('returns the leader schedule for only the specified node in the current epoch', async () => {
                    expect.assertions(1);
                    const identity = getValidatorAddress();
                    const res = await rpc
                        .getLeaderSchedule({
                            commitment,
                            identity,
                        })
                        .send();
                    // Does not need null check (default slot)
                    expect(res).toMatchObject({
                        [identity]: expect.any(Array),
                    });
                });
            });

            describe('when called with an account that is a validator identity and a valid slot', () => {
                it('returns the leader schedule for only the specified node in the epoch corresponding to the provided slot', async () => {
                    expect.assertions(1);
                    const identity = getValidatorAddress();
                    const res = await rpc
                        .getLeaderSchedule(0n, {
                            commitment,
                            identity,
                        })
                        .send();
                    // Needs null check (slot provided and may correspond to epoch that does not exist)
                    assert(res);
                    expect(res).toMatchObject({
                        [identity]: expect.any(Array),
                    });
                });
            });
        });

        describe('given an account that exists but is not a validator identity', () => {
            it('returns an empty object', async () => {
                expect.assertions(1);
                const res = await rpc
                    .getLeaderSchedule({
                        commitment,
                        // See scripts/fixtures/GQE2yjns7SKKuMc89tveBDpzYHwXfeuB2PGAbGaPWc6G.json
                        identity: 'GQE2yjns7SKKuMc89tveBDpzYHwXfeuB2PGAbGaPWc6G' as Base58EncodedAddress,
                    })
                    .send();
                expect(res).toMatchObject({});
            });
        });

        describe('given an account that does not exist', () => {
            it('returns an empty object', async () => {
                expect.assertions(1);
                const res = await rpc
                    .getLeaderSchedule({
                        commitment,
                        // Randomly generated
                        identity: 'BnWCFuxmi6uH3ceVx4R8qcbWBMPVVYVVFWtAiiTA1PAu' as Base58EncodedAddress,
                    })
                    .send();
                expect(res).toMatchObject({});
            });
        });

        describe('given an invalid slot', () => {
            it('returns an empty object', async () => {
                expect.assertions(1);
                const leaderSchedulePromise = rpc
                    .getLeaderSchedule(
                        2n ** 63n - 1n, // u64:MAX; safe bet it'll be too high.
                        { commitment }
                    )
                    .send();
                await expect(leaderSchedulePromise).resolves.toBeNull();
            });
        });
    });
});


