apps/payment-ui/src/errors/socket-connected-without-payment-id.error.ts
=======================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export class SocketConnectedWithoutPaymentIdError extends Error {
    constructor() {
        super();
        this.name = 'SocketConnectedWithoutPaymentIdError';
    }
}


