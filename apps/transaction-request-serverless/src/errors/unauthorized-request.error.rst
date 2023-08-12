apps/transaction-request-serverless/src/errors/unauthorized-request.error.ts
============================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class UnauthorizedRequestError extends Error {
    constructor(reason: string) {
        super(`Unauthorized Request Reason: ${reason}`);
        this.name = 'UnauthorizedRequestError';
        Object.setPrototypeOf(this, UnauthorizedRequestError.prototype);
    }
}


