packages/rpc-core/src/stringified-bigint.ts
===========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    export type StringifiedBigInt = string & { readonly __bigint: unique symbol };

export function assertIsStringifiedBigInt(putativeBigInt: string): asserts putativeBigInt is StringifiedBigInt {
    try {
        BigInt(putativeBigInt);
    } catch (e) {
        throw new Error(`\`${putativeBigInt}\` cannot be parsed as a BigInt`, {
            cause: e,
        });
    }
}


