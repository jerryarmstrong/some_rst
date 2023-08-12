apps/transaction-request-serverless/src/errors/missing-env.error.ts
===================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class MissingEnvError extends Error {
    constructor(envName: string) {
        super(`Missing environment variable: ${envName}`);
        this.name = 'MissingEnvError';
        Object.setPrototypeOf(this, MissingEnvError.prototype);
    }
}


