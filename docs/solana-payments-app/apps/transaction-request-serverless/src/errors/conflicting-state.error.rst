apps/transaction-request-serverless/src/errors/conflicting-state.error.ts
=========================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class ConflictingStateError extends Error {
    constructor(issue: string) {
        super(`Conflicting issue: ${issue}`);
        this.name = 'ConflictingStateError';
        Object.setPrototypeOf(this, ConflictingStateError.prototype);
    }
}


