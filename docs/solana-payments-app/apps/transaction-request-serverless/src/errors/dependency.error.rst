apps/transaction-request-serverless/src/errors/dependency.error.ts
==================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class DependencyError extends Error {
    constructor(dependencyName: string) {
        super(`Issue with dependency: ${dependencyName}`);
        this.name = 'DependencyError';
        Object.setPrototypeOf(this, DependencyError.prototype);
    }
}


