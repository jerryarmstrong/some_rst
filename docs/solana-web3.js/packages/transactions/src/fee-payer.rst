packages/transactions/src/fee-payer.ts
======================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';

import { ITransactionWithSignatures } from './signatures';
import { BaseTransaction } from './types';
import { getUnsignedTransaction } from './unsigned-transaction';

export interface ITransactionWithFeePayer<TAddress extends string = string> {
    readonly feePayer: Base58EncodedAddress<TAddress>;
}

export function setTransactionFeePayer<TFeePayerAddress extends string, TTransaction extends BaseTransaction>(
    feePayer: Base58EncodedAddress<TFeePayerAddress>,
    transaction:
        | TTransaction
        | (TTransaction & ITransactionWithFeePayer<TFeePayerAddress>)
        | (TTransaction & ITransactionWithSignatures)
        | (TTransaction & ITransactionWithFeePayer<TFeePayerAddress> & ITransactionWithSignatures)
):
    | (TTransaction & ITransactionWithFeePayer<TFeePayerAddress>)
    | (Omit<TTransaction, keyof ITransactionWithSignatures> & ITransactionWithFeePayer<TFeePayerAddress>) {
    if ('feePayer' in transaction && feePayer === transaction.feePayer) {
        return transaction;
    }
    const out = {
        ...getUnsignedTransaction(transaction),
        feePayer,
    };
    Object.freeze(out);
    return out;
}


