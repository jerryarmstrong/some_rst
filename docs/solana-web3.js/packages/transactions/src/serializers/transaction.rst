packages/transactions/src/serializers/transaction.ts
====================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { array, bytes, Serializer, shortU16, struct } from '@metaplex-foundation/umi-serializers';

import { getCompiledTransaction } from '../compile-transaction';
import { getCompiledMessageEncoder } from './message';
import { getUnimplementedDecoder } from './unimplemented';

const BASE_CONFIG = {
    description: __DEV__ ? 'The wire format of a Solana transaction' : '',
    fixedSize: null,
    maxSize: null,
} as const;

type SerializableTransaction = Parameters<typeof getCompiledTransaction>[0];

function serialize(transaction: SerializableTransaction) {
    const compiledTransaction = getCompiledTransaction(transaction);
    return struct([
        [
            'signatures',
            array(bytes({ size: 64 }), {
                ...(__DEV__ ? { description: 'A compact array of 64-byte, base-64 encoded Ed25519 signatures' } : null),
                size: shortU16(),
            }),
        ],
        ['compiledMessage', getCompiledMessageEncoder()],
    ]).serialize(compiledTransaction);
}

export function getTransactionEncoder(): Serializer<SerializableTransaction> {
    return {
        ...BASE_CONFIG,
        deserialize: getUnimplementedDecoder('CompiledMessage'),
        serialize,
    };
}


