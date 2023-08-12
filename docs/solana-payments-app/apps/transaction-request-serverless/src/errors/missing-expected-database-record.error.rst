apps/transaction-request-serverless/src/errors/missing-expected-database-record.error.ts
========================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class MissingExpectedDatabaseRecordError extends Error {
    constructor(databaseRecordName: string) {
        super(`Missing expected database record: ${databaseRecordName}`);
        this.name = 'MissingExpectedDatabaseRecordError';
        Object.setPrototypeOf(this, MissingExpectedDatabaseRecordError.prototype);
    }
}


