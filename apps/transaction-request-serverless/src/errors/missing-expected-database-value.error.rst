apps/transaction-request-serverless/src/errors/missing-expected-database-value.error.ts
=======================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class MissingExpectedDatabaseValueError extends Error {
    constructor(databaseValueName: string) {
        super(`Missing expected database value: ${databaseValueName}`);
        this.name = 'MissingExpectedDatabaseValueError';
        Object.setPrototypeOf(this, MissingExpectedDatabaseValueError.prototype);
    }
}


