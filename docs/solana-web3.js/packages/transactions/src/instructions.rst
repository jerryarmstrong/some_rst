packages/transactions/src/instructions.ts
=========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { ITransactionWithSignatures } from './signatures';
import { BaseTransaction } from './types';
import { getUnsignedTransaction } from './unsigned-transaction';

export function appendTransactionInstruction<TTransaction extends BaseTransaction>(
    instruction: TTransaction['instructions'][number],
    transaction: TTransaction | (TTransaction & ITransactionWithSignatures)
): TTransaction | Omit<TTransaction, keyof ITransactionWithSignatures> {
    const out = {
        ...getUnsignedTransaction(transaction),
        instructions: [...transaction.instructions, instruction],
    };
    Object.freeze(out);
    return out;
}

export function prependTransactionInstruction<TTransaction extends BaseTransaction>(
    instruction: TTransaction['instructions'][number],
    transaction: TTransaction | (TTransaction & ITransactionWithSignatures)
): TTransaction | Omit<TTransaction, keyof ITransactionWithSignatures> {
    const out = {
        ...getUnsignedTransaction(transaction),
        instructions: [instruction, ...transaction.instructions],
    };
    Object.freeze(out);
    return out;
}


