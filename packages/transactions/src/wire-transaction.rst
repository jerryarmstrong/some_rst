packages/transactions/src/wire-transaction.ts
=============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { getTransactionEncoder } from './serializers/transaction';

export type Base64EncodedWireTransaction = string & {
    readonly __base64EncodedWireTransaction: unique symbol;
};

export function getBase64EncodedWireTransaction(
    transaction: Parameters<ReturnType<typeof getTransactionEncoder>['serialize']>[0]
): Base64EncodedWireTransaction {
    const wireTransactionBytes = getTransactionEncoder().serialize(transaction);
    if (__NODEJS__) {
        return Buffer.from(wireTransactionBytes).toString('base64') as Base64EncodedWireTransaction;
    } else {
        return (btoa as Window['btoa'])(String.fromCharCode(...wireTransactionBytes)) as Base64EncodedWireTransaction;
    }
}


