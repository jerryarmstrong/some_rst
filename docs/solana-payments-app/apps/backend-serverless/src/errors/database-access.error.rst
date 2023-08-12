apps/backend-serverless/src/errors/database-access.error.ts
===========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class DatabaseAccessError extends Error {
    constructor(recordName: string) {
        super(`Issue with record: ${recordName}`);
        this.name = 'DatabaseAccessError';
        Object.setPrototypeOf(this, DatabaseAccessError.prototype);
    }
}


