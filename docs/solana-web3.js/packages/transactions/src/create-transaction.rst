packages/transactions/src/create-transaction.ts
===============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Transaction, TransactionVersion } from './types';

type TransactionConfig<TVersion extends TransactionVersion> = Readonly<{
    version: TVersion;
}>;

export function createTransaction<TVersion extends TransactionVersion>(
    config: TransactionConfig<TVersion>
): Extract<Transaction, { version: TVersion }>;
export function createTransaction<TVersion extends TransactionVersion>({
    version,
}: TransactionConfig<TVersion>): Transaction {
    const out: Transaction = {
        instructions: [],
        version,
    };
    Object.freeze(out);
    return out;
}


