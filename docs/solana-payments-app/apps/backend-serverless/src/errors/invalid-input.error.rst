apps/backend-serverless/src/errors/invalid-input.error.ts
=========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class InvalidInputError extends Error {
    constructor(envName: string) {
        super(`Invalid input error: ${envName}`);
        this.name = 'InvalidInputError';
        Object.setPrototypeOf(this, InvalidInputError.prototype);
    }
}


