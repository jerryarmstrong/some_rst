packages/rpc-core/src/transaction-signature.ts
==============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { base58 } from '@metaplex-foundation/umi-serializers';

export type TransactionSignature = string & { readonly __sig: unique symbol };

export function assertIsTransactionSignature(
    putativeTransactionSignature: string
): asserts putativeTransactionSignature is TransactionSignature {
    try {
        // Fast-path; see if the input string is of an acceptable length.
        if (
            // Lowest value (64 bytes of zeroes)
            putativeTransactionSignature.length < 64 ||
            // Highest value (64 bytes of 255)
            putativeTransactionSignature.length > 88
        ) {
            throw new Error('Expected input string to decode to a byte array of length 64.');
        }
        // Slow-path; actually attempt to decode the input string.
        const bytes = base58.serialize(putativeTransactionSignature);
        const numBytes = bytes.byteLength;
        if (numBytes !== 64) {
            throw new Error(`Expected input string to decode to a byte array of length 64. Actual length: ${numBytes}`);
        }
    } catch (e) {
        throw new Error(`\`${putativeTransactionSignature}\` is not a transaction signature`, {
            cause: e,
        });
    }
}


