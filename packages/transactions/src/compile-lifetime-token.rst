packages/transactions/src/compile-lifetime-token.ts
===================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { IDurableNonceTransaction, ITransactionWithBlockhashLifetime } from './index';

export function getCompiledLifetimeToken(
    lifetimeConstraint: (ITransactionWithBlockhashLifetime | IDurableNonceTransaction)['lifetimeConstraint']
): string {
    if ('nonce' in lifetimeConstraint) {
        return lifetimeConstraint.nonce;
    }
    return lifetimeConstraint.blockhash;
}


