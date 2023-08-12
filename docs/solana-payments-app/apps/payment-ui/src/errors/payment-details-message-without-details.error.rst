apps/payment-ui/src/errors/payment-details-message-without-details.error.ts
===========================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class PaymentDetailsMessageWithoutDetailsError extends Error {
    constructor() {
        super();
        this.name = 'PaymentDetailsMessageWithoutDetailsError';
    }
}


