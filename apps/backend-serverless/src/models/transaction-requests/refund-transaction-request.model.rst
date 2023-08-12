apps/backend-serverless/src/models/transaction-requests/refund-transaction-request.model.ts
===========================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object, string } from 'yup';
import { parseAndValidateStrict } from '../../utilities/yup.utility.js';

export const refundTransactionRequestScheme = object().shape({
    refundId: string().required(),
});

export type RefundTransactionRequest = InferType<typeof refundTransactionRequestScheme>;

export const parseAndValidateRefundTransactionRequest = (
    refundTransactionRequestBody: unknown,
): RefundTransactionRequest => {
    return parseAndValidateStrict<RefundTransactionRequest>(
        refundTransactionRequestBody,
        refundTransactionRequestScheme,
        'Could not parse the refund transaction request body. Unknown Reason.',
    );
};


