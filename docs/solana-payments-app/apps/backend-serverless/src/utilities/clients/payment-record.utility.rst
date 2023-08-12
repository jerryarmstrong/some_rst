apps/backend-serverless/src/utilities/clients/payment-record.utility.ts
=======================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { PaymentRecord } from '@prisma/client';

export interface PaymentDataResponse {
    shopifyOrder: string;
    requestedAt: Date;
    completedAt?: Date;
    status: string;
    amount: string;
    transactionSignature?: string;
}

export const createPaymentDataResponseFromPaymentRecord = (paymentRecord: PaymentRecord): PaymentDataResponse => {
    return {
        shopifyOrder: paymentRecord.shopId,
        requestedAt: paymentRecord.requestedAt,
        ...(paymentRecord.completedAt && { completedAt: paymentRecord.completedAt }),
        status: paymentRecord.status,
        amount: paymentRecord.amount ? `${paymentRecord.amount} ${paymentRecord.currency}` : 'Not Availible',
        ...(paymentRecord.transactionSignature && { transactionSignature: paymentRecord.transactionSignature }),
    };
};


