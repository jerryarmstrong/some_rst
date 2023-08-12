packages/rpc-core/src/rpc-methods/__tests__/get-fee-for-message-test.ts
=======================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { base58, base64, fixSerializer } from '@metaplex-foundation/umi-serializers';
import { createHttpTransport, createJsonRpc } from '@solana/rpc-transport';
import type { SolanaJsonRpcErrorCode } from '@solana/rpc-transport/dist/types/json-rpc-errors';
import type { Rpc } from '@solana/rpc-transport/dist/types/json-rpc-types';
import { Blockhash } from '@solana/transactions';
import fetchMock from 'jest-fetch-mock-fork';

import { Base64EncodedBytes, Commitment } from '../common';
import { createSolanaRpcApi, SolanaRpcMethods } from '../index';

// See scripts/fixtures/send-transaction-fee-payer.json
const MOCK_PUBLIC_KEY_BYTES = // DRtXHDgC312wpNdNCSb8vCoXDcofCJcPHdAw4VkJ8L9i
    // prettier-ignore
    new Uint8Array([
        0xb8, 0xac, 0x70, 0x4f, 0xaf, 0xc7, 0xa5, 0xfc, 0x8c, 0x5d, 0x1f, 0x0a, 0xc8, 0xcf, 0xaa, 0xe0,
        0x42, 0xfa, 0x3b, 0xb8, 0x25, 0xf0, 0xec, 0xfc, 0xe2, 0x27, 0x4d, 0x7d, 0xad, 0xad, 0x51, 0x2d,
    ]);

function getMockTransactionMessage(blockhash: Blockhash) {
    const memoString = 'Hello from the web3.js tests!';
    const blockhashBytes = fixSerializer(base58, 32).serialize(blockhash);
    // prettier-ignore
    const message = new Uint8Array([
        /** VERSION HEADER */
        0x80, // 0 + version mask

        /** MESSAGE HEADER */
        0x01, // numSignerAccounts
        0x00, // numReadonlySignerAccount
        0x01, // numReadonlyNonSignerAccounts

        /** STATIC ADDRESSES */
        0x02, // Number of static accounts
            ...MOCK_PUBLIC_KEY_BYTES,
            0x05, 0x4a, 0x53, 0x5a, 0x99, 0x29, 0x21, 0x06, 0x4d, 0x24, 0xe8, 0x71, 0x60, 0xda, 0x38, 0x7c, 0x7c, 0x35, 0xb5, 0xdd, 0xbc, 0x92, 0xbb, 0x81, 0xe4, 0x1f, 0xa8, 0x40, 0x41, 0x05, 0x44, 0x8d, // MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr

        /** TRANSACTION LIFETIME TOKEN (ie. the blockhash) */
        ...blockhashBytes,

        /* INSTRUCTIONS */
        0x01, // Number of instructions

            // First instruction
            0x01, // Program address index
            0x00, // Number of address indices
            memoString.length, // Length of instruction data
                ...new TextEncoder().encode(memoString),

        /** ADDRESS TABLE LOOKUPS */
        0x00, // Number of address table lookups
    ]);
    const messageBase64 = base64.deserialize(message)[0];
    return messageBase64 as Base64EncodedBytes;
}

describe('getFeeForMessage', () => {
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
            if (commitment === 'finalized') {
                it.todo(
                    'returns the result as a bigint (test broken; see https://discord.com/channels/428295358100013066/560496939779620864/1132048104728825926)'
                );
                return;
            }
            describe('when called with a recent blockhash', () => {
                it('returns the result as a bigint', async () => {
                    expect.assertions(1);
                    const latestBlockhash = await rpc.getLatestBlockhash().send();
                    const message = getMockTransactionMessage(latestBlockhash.value.blockhash);
                    console.log('Printing mock message', message);
                    const result = await rpc.getFeeForMessage(message, { commitment }).send();
                    expect(result).toMatchObject({
                        context: {
                            slot: expect.any(BigInt),
                        },
                        value: expect.any(BigInt),
                    });
                });
            });

            describe('when called with an old blockhash', () => {
                // TODO: There's no way to deterministically get an old blockhash
                it.todo('returns null');
            });

            describe('when called with a blockhash that does not exist', () => {
                it('returns null', async () => {
                    expect.assertions(1);
                    const message = getMockTransactionMessage(
                        // Randomly generated
                        'BnWCFuxmi6uH3ceVx4R8qcbWBMPVVYVVFWtAiiTA1PAu' as Blockhash
                    );
                    const result = await rpc.getFeeForMessage(message, { commitment }).send();
                    expect(result).toMatchObject({
                        context: {
                            slot: expect.any(BigInt),
                        },
                        value: null,
                    });
                });
            });
        });
    });

    describe('when called with an invalid message', () => {
        it('throws an error', async () => {
            expect.assertions(1);
            const sendPromise = rpc.getFeeForMessage('someInvalidMessage' as Base64EncodedBytes).send();
            await expect(sendPromise).rejects.toMatchObject({
                code: -32602 satisfies (typeof SolanaJsonRpcErrorCode)['JSON_RPC_INVALID_PARAMS'],
                message: expect.any(String),
                name: 'SolanaJsonRpcError',
            });
        });
    });

    describe('when called with a `minContextSlot` higher than the highest slot available', () => {
        it('throws an error', async () => {
            expect.assertions(1);
            const latestBlockhash = await rpc.getLatestBlockhash().send();
            const message = getMockTransactionMessage(latestBlockhash.value.blockhash);
            const sendPromise = rpc
                .getFeeForMessage(message, {
                    minContextSlot: 2n ** 63n - 1n, // u64:MAX; safe bet it'll be too high.
                })
                .send();
            await expect(sendPromise).rejects.toMatchObject({
                code: -32016 satisfies (typeof SolanaJsonRpcErrorCode)['JSON_RPC_SERVER_ERROR_MIN_CONTEXT_SLOT_NOT_REACHED'],
                message: expect.any(String),
                name: 'SolanaJsonRpcError',
            });
        });
    });
});


