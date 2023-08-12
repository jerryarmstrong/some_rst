packages/transactions/src/serializers/__tests__/message-test.ts
===============================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Serializer } from '@metaplex-foundation/umi-serializers';
import { Base58EncodedAddress } from '@solana/addresses';

import { CompiledMessage } from '../../message';
import { getCompiledMessageCodec, getCompiledMessageDecoder, getCompiledMessageEncoder } from '../message';

describe.each([getCompiledMessageCodec, getCompiledMessageEncoder])(
    'Transaction message serializer %p',
    serializerFactory => {
        let compiledMessage: Serializer<CompiledMessage>;
        beforeEach(() => {
            compiledMessage = serializerFactory();
        });
        it('serializes a transaction according to the spec', () => {
            const byteArray = compiledMessage.serialize({
                addressTableLookups: [
                    {
                        lookupTableAddress: '3yS1JFVT284y8z1LC9MRoWxZjzFrdoD5axKsZiyMsfC7' as Base58EncodedAddress, // decodes to [44{32}]
                        readableIndices: [77],
                        writableIndices: [66, 55],
                    },
                ],
                header: {
                    numReadonlyNonSignerAccounts: 1,
                    numReadonlySignerAccounts: 2,
                    numSignerAccounts: 3,
                },
                instructions: [
                    { programAddressIndex: 44 },
                    { accountIndices: [77, 66], data: new Uint8Array([7, 8, 9]), programAddressIndex: 55 },
                ],
                lifetimeToken: '3EKkiwNLWqoUbzFkPrmKbtUB4EweE6f4STzevYUmezeL', // decodes to [33{32}]
                staticAccounts: [
                    'k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn', // decodes to [11{32}]
                    '2VDW9dFE1ZXz4zWAbaBDQFynNVdRpQ73HyfSHMzBSL6Z', // decodes to [22{32}]
                ] as Base58EncodedAddress[],
                version: 0,
            });
            expect(byteArray).toStrictEqual(
                // prettier-ignore
                new Uint8Array([
                    /** VERSION HEADER */
                    128, // 0 + version mask

                    /** MESSAGE HEADER */
                    3, // numSignerAccounts
                    2, // numReadonlySignerAccount
                    1, // numReadonlyNonSignerAccounts

                    /** STATIC ADDRESSES */
                    2, // Number of static accounts
                        11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, // k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn
                        22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, // 2VDW9dFE1ZXz4zWAbaBDQFynNVdRpQ73HyfSHMzBSL6Z

                    /** TRANSACTION LIFETIME TOKEN (ie. the blockhash) */
                    33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, // 3EKkiwNLWqoUbzFkPrmKbtUB4EweE6f4STzevYUmezeL

                    /* INSTRUCTIONS */
                    2, // Number of instructions

                        // First instruction
                        44, // Program address index
                        0, // Number of address indices
                        0, // Length of instruction data

                        // Second instruction
                        55, // Program address index
                        2, // Number of address indices
                            77, 66, // Address indices
                        3, // Length of instruction data
                            7, 8, 9, // Instruction data itself

                    /** ADDRESS TABLE LOOKUPS */
                    1, // Number of address table lookups

                        // First address table lookup
                        44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, // Address of lookup table 3yS1JFVT284y8z1LC9MRoWxZjzFrdoD5axKsZiyMsfC7
                        2, // Number of writable indices
                            66, 55, // Writable indices
                        1, // Number of readonly indices
                            77, // Readonly indices
                ])
            );
        });
        it('serializes a versioned transaction with `undefined` address table lookups', () => {
            const byteArray = compiledMessage.serialize({
                /** `addressTableLookups` is not defined */
                header: {
                    numReadonlyNonSignerAccounts: 1,
                    numReadonlySignerAccounts: 2,
                    numSignerAccounts: 3,
                },
                instructions: [],
                lifetimeToken: 'k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn', // decodes to [11{32}]
                staticAccounts: [],
                version: 0,
            });
            expect(byteArray).toStrictEqual(
                // prettier-ignore
                new Uint8Array([
                    /** VERSION HEADER */
                    128, // 0 + version mask

                    /** MESSAGE HEADER */
                    3, // numSignerAccounts
                    2, // numReadonlySignerAccount
                    1, // numReadonlyNonSignerAccounts

                    /** STATIC ADDRESSES */
                    0, // Number of static accounts

                    /** TRANSACTION LIFETIME TOKEN (ie. the blockhash) */
                    11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, // 3EKkiwNLWqoUbzFkPrmKbtUB4EweE6f4STzevYUmezeL

                    /* INSTRUCTIONS */
                    0, // Number of instructions

                    /** ADDRESS TABLE LOOKUPS get serialized despite not being in the source object */
                    0, // Number of address table lookups
                ])
            );
        });
        it('omits the version header for `legacy` transactions', () => {
            expect(
                compiledMessage.serialize({
                    header: {
                        numReadonlyNonSignerAccounts: 1,
                        numReadonlySignerAccounts: 2,
                        numSignerAccounts: 3,
                    },
                    instructions: [],
                    lifetimeToken: 'k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn', // decodes to [11{32}]
                    staticAccounts: [],
                    version: 'legacy',
                })
            ).toStrictEqual(
                // prettier-ignore
                new Uint8Array([
                    /** NO VERSION HEADER */

                    /** MESSAGE HEADER */
                    3, // numSignerAccounts
                    2, // numReadonlySignerAccount
                    1, // numReadonlyNonSignerAccounts

                    /** STATIC ADDRESSES */
                    0, // Number of static accounts

                    /** TRANSACTION LIFETIME TOKEN (ie. the blockhash) */
                    11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, // k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn

                    /* INSTRUCTIONS */
                    0, // Number of instructions
                ])
            );
        });
        it('omits the address table lookups for `legacy` transactions', () => {
            expect(
                getCompiledMessageCodec().serialize({
                    header: {
                        numReadonlyNonSignerAccounts: 1,
                        numReadonlySignerAccounts: 2,
                        numSignerAccounts: 3,
                    },
                    instructions: [],
                    lifetimeToken: 'k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn', // decodes to [11{32}]
                    staticAccounts: [],
                    version: 'legacy',
                })
            ).toStrictEqual(
                // prettier-ignore
                new Uint8Array([
                    /** MESSAGE HEADER */
                    3, // numSignerAccounts
                    2, // numReadonlySignerAccount
                    1, // numReadonlyNonSignerAccounts

                    /** STATIC ADDRESSES */
                    0, // Number of static accounts

                    /** TRANSACTION LIFETIME TOKEN (ie. the blockhash) */
                    11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, // k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn

                    /* INSTRUCTIONS */
                    0, // Number of instructions

                    /** NO ADDRESS TABLE LOOKUPS */
                ])
            );
        });
    }
);

describe.each([getCompiledMessageCodec, getCompiledMessageDecoder])(
    'Transaction message deserializer %p',
    serializerFactory => {
        let compiledMessage: Serializer<CompiledMessage>;
        beforeEach(() => {
            compiledMessage = serializerFactory();
        });
        it('deserializes a version 0 transaction according to the spec', () => {
            const byteArray =
                // prettier-ignore
                new Uint8Array([
                    /** VERSION HEADER */
                    128, // 0 + version mask

                    /** MESSAGE HEADER */
                    3, // numSignerAccounts
                    2, // numReadonlySignerAccount
                    1, // numReadonlyNonSignerAccounts

                    /** STATIC ADDRESSES */
                    2, // Number of static accounts
                        11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, // k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn
                        22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, // 2VDW9dFE1ZXz4zWAbaBDQFynNVdRpQ73HyfSHMzBSL6Z

                    /** TRANSACTION LIFETIME TOKEN (ie. the blockhash) */
                    33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, // 3EKkiwNLWqoUbzFkPrmKbtUB4EweE6f4STzevYUmezeL

                    /* INSTRUCTIONS */
                    2, // Number of instructions

                        // First instruction
                        44, // Program address index
                        0, // Number of address indices
                        0, // Length of instruction data

                        // Second instruction
                        55, // Program address index
                        2, // Number of address indices
                            77, 66, // Address indices
                        3, // Length of instruction data
                            7, 8, 9, // Instruction data itself

                    /** ADDRESS TABLE LOOKUPS */
                    1, // Number of address table lookups

                        // First address table lookup
                        44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, // Address of lookup table 3yS1JFVT284y8z1LC9MRoWxZjzFrdoD5axKsZiyMsfC7
                        2, // Number of writable indices
                            66, 55, // Writable indices
                        1, // Number of readonly indices
                            77, // Readonly indices
                ]);
            const [message, offset] = compiledMessage.deserialize(byteArray);
            expect(message).toStrictEqual({
                addressTableLookups: [
                    {
                        lookupTableAddress: '3yS1JFVT284y8z1LC9MRoWxZjzFrdoD5axKsZiyMsfC7' as Base58EncodedAddress, // decodes to [44{32}]
                        readableIndices: [77],
                        writableIndices: [66, 55],
                    },
                ],
                header: {
                    numReadonlyNonSignerAccounts: 1,
                    numReadonlySignerAccounts: 2,
                    numSignerAccounts: 3,
                },
                instructions: [
                    { programAddressIndex: 44 },
                    { accountIndices: [77, 66], data: new Uint8Array([7, 8, 9]), programAddressIndex: 55 },
                ],
                lifetimeToken: '3EKkiwNLWqoUbzFkPrmKbtUB4EweE6f4STzevYUmezeL', // decodes to [33{32}]
                staticAccounts: [
                    'k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn', // decodes to [11{32}]
                    '2VDW9dFE1ZXz4zWAbaBDQFynNVdRpQ73HyfSHMzBSL6Z', // decodes to [22{32}]
                ] as Base58EncodedAddress[],
                version: 0,
            });
            // Expect the entire byte array to have been consumed.
            expect(offset).toBe(byteArray.byteLength);
        });
        it('omits the `addressTableLookups` property of a versioned transaction when the address table lookups are zero-length', () => {
            expect(
                compiledMessage.deserialize(
                    // prettier-ignore
                    new Uint8Array([
                        /** VERSION HEADER */
                        128, // 0 + version mask

                        /** MESSAGE HEADER */
                        3, // numSignerAccounts
                        2, // numReadonlySignerAccount
                        1, // numReadonlyNonSignerAccounts

                        /** STATIC ADDRESSES */
                        0, // Number of static accounts

                        /** TRANSACTION LIFETIME TOKEN (ie. the blockhash) */
                        33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, // 3EKkiwNLWqoUbzFkPrmKbtUB4EweE6f4STzevYUmezeL

                        /* INSTRUCTIONS */
                        0, // Number of instructions
                    ])
                )[0]
            ).not.toHaveProperty('addressTableLookups');
        });
        it('deserializes a legacy transaction according to the spec', () => {
            const byteArray =
                // prettier-ignore
                new Uint8Array([
                    /** MESSAGE HEADER */
                    3, // numSignerAccounts
                    2, // numReadonlySignerAccount
                    1, // numReadonlyNonSignerAccounts

                    /** STATIC ADDRESSES */
                    2, // Number of static accounts
                        11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, // k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn
                        22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, // 2VDW9dFE1ZXz4zWAbaBDQFynNVdRpQ73HyfSHMzBSL6Z

                    /** TRANSACTION LIFETIME TOKEN (ie. the blockhash) */
                    33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, // 3EKkiwNLWqoUbzFkPrmKbtUB4EweE6f4STzevYUmezeL

                    /* INSTRUCTIONS */
                    2, // Number of instructions

                        // First instruction
                        44, // Program address index
                        0, // Number of address indices
                        0, // Length of instruction data

                        // Second instruction
                        55, // Program address index
                        2, // Number of address indices
                            77, 66, // Address indices
                        3, // Length of instruction data
                            7, 8, 9, // Instruction data itself
                ]);
            const [message, offset] = compiledMessage.deserialize(byteArray);
            expect(message).toStrictEqual({
                header: {
                    numReadonlyNonSignerAccounts: 1,
                    numReadonlySignerAccounts: 2,
                    numSignerAccounts: 3,
                },
                instructions: [
                    { programAddressIndex: 44 },
                    { accountIndices: [77, 66], data: new Uint8Array([7, 8, 9]), programAddressIndex: 55 },
                ],
                lifetimeToken: '3EKkiwNLWqoUbzFkPrmKbtUB4EweE6f4STzevYUmezeL', // decodes to [33{32}]
                staticAccounts: [
                    'k7FaK87WHGVXzkaoHb7CdVPgkKDQhZ29VLDeBVbDfYn', // decodes to [11{32}]
                    '2VDW9dFE1ZXz4zWAbaBDQFynNVdRpQ73HyfSHMzBSL6Z', // decodes to [22{32}]
                ] as Base58EncodedAddress[],
                version: 'legacy',
            });
            // Expect the entire byte array to have been consumed.
            expect(offset).toBe(byteArray.byteLength);
        });
    }
);

describe('The transaction message decode-only factory', () => {
    it('throws when you call `serialize`', () => {
        expect(getCompiledMessageDecoder().serialize).toThrowErrorMatchingInlineSnapshot(
            `"No encoder exists for CompiledMessage. Use \`getCompiledMessageEncoder()\` if you need a encoder, and \`getCompiledMessageCodec()\` if you need to both encode and decode CompiledMessage"`
        );
    });
});

describe('The transaction message encode-only factory', () => {
    it('throws when you call `deserialize`', () => {
        expect(getCompiledMessageEncoder().deserialize).toThrowErrorMatchingInlineSnapshot(
            `"No decoder exists for CompiledMessage. Use \`getCompiledMessageDecoder()\` if you need a decoder, and \`getCompiledMessageCodec()\` if you need to both encode and decode CompiledMessage"`
        );
    });
});


