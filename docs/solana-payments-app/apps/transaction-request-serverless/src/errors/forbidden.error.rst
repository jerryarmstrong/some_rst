apps/transaction-request-serverless/src/errors/forbidden.error.ts
=================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class ForbiddenError extends Error {
    constructor() {
        super();
        this.name = 'ForbiddenError';
        Object.setPrototypeOf(this, ForbiddenError.prototype);
    }
}


