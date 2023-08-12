apps/backend-serverless/src/models/clients/merchant-ui/payment-data-request.model.ts
====================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, number, object } from 'yup';
import { DEFAULT_PAGINATION_SIZE } from '../../../utilities/clients/database-services.utility.js';
import { parseAndValidateStrict } from '../../../utilities/yup.utility.js';

const parseParameters = (params: any) => {
    return {
        pageNumber: parseInt(params.pageNumber),
        pageSize: parseInt(params.pageSize),
    };
};

export const paymentDataRequestParametersSchema = object().shape({
    pageNumber: number().min(1).default(-1),
    pageSize: number().min(1).default(DEFAULT_PAGINATION_SIZE),
});

export type PaymentDataRequestParameters = InferType<typeof paymentDataRequestParametersSchema>;

export const parseAndValidatePaymentDataRequestParameters = (
    paymentDataRequestParametersBody: any
): PaymentDataRequestParameters => {
    return parseAndValidateStrict(
        parseParameters(paymentDataRequestParametersBody),
        paymentDataRequestParametersSchema,
        'Could not parse the payment data request parameters. Unknown Reason.'
    );
};


