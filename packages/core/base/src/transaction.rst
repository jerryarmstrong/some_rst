packages/core/base/src/transaction.ts
=====================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: ts

    import type { Transaction, TransactionVersion, VersionedTransaction } from '@solana/web3.js';

export type SupportedTransactionVersions = ReadonlySet<TransactionVersion> | null | undefined;

export type TransactionOrVersionedTransaction<S extends SupportedTransactionVersions> = S extends null | undefined
    ? Transaction
    : Transaction | VersionedTransaction;

export function isVersionedTransaction(
    transaction: Transaction | VersionedTransaction
): transaction is VersionedTransaction {
    return 'version' in transaction;
}


