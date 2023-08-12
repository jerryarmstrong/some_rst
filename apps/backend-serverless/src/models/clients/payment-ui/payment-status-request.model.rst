apps/backend-serverless/src/models/clients/payment-ui/payment-status-request.model.ts
=====================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object, string } from 'yup';
import { parseAndValidateStrict } from '../../../utilities/yup.utility.js';

export const paymentStatusRequestScheme = object().shape({
    paymentId: string().required(),
    language: string().required(),
});

export type PaymentStatusRequest = InferType<typeof paymentStatusRequestScheme>;

export const parseAndValidatePaymentStatusRequest = (paymentStatusRequestParameters: unknown): PaymentStatusRequest => {
    return parseAndValidateStrict(
        paymentStatusRequestParameters,
        paymentStatusRequestScheme,
        'Can not parse payment status request. Unkownn reason.',
    );
};


