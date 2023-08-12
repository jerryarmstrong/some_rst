apps/backend-serverless/src/models/clients/merchant-ui/refund-status-request.model.ts
=====================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object, string } from 'yup';
import { parseAndValidateStrict } from '../../../utilities/yup.utility.js';

export const refundStatusRequestScheme = object().shape({
    shopId: string().required(),
});

export type RefundStatusRequest = InferType<typeof refundStatusRequestScheme>;

export const parseAndValidateRefundStatusRequest = (refundStatusRequestParameters: unknown): RefundStatusRequest => {
    return parseAndValidateStrict<RefundStatusRequest>(
        refundStatusRequestParameters,
        refundStatusRequestScheme,
        'Could not parse the refund status request parameters. Unknown Reason.',
    );
};


