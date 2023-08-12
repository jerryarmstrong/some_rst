packages/transactions/src/unsigned-transaction.ts
=================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { ITransactionWithSignatures } from '.';
import { BaseTransaction } from './types';

export function getUnsignedTransaction<TTransaction extends BaseTransaction>(
    transaction: TTransaction | (TTransaction & ITransactionWithSignatures)
): TTransaction | Omit<TTransaction & ITransactionWithSignatures, keyof ITransactionWithSignatures> {
    if ('signatures' in transaction) {
        // The implication of the lifetime constraint changing is that any existing signatures are invalid.
        const {
            signatures: _, // eslint-disable-line @typescript-eslint/no-unused-vars
            ...unsignedTransaction
        } = transaction;
        return unsignedTransaction;
    } else {
        return transaction;
    }
}


