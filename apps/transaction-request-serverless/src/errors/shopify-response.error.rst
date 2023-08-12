apps/transaction-request-serverless/src/errors/shopify-response.error.ts
========================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class ShopifyResponseError extends Error {
    constructor(type: string) {
        super(`Shopify response error: ${type}`);
        this.name = 'ShopifyResponseError';
        Object.setPrototypeOf(this, ShopifyResponseError.prototype);
    }
}


