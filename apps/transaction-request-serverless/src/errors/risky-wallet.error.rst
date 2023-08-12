apps/transaction-request-serverless/src/errors/risky-wallet.error.ts
====================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class RiskyWalletError extends Error {
    constructor() {
        super(`Wallet is not safe to tranansaction with`);
        this.name = 'RiskyWalletError';
        Object.setPrototypeOf(this, RiskyWalletError.prototype);
    }
}


