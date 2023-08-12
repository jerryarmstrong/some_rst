apps/backend-serverless/src/models/clients/merchant-ui/refund-data-request.model.ts
===================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, number, object, string } from 'yup';
import { RefundStatusOption } from '../../../utilities/clients/create-refund-response.utility.js';
import { DEFAULT_PAGINATION_SIZE } from '../../../utilities/clients/database-services.utility.js';
import { parseAndValidateStrict } from '../../../utilities/yup.utility.js';

const parseParameters = params => {
    return {
        pageNumber: parseInt(params.pageNumber),
        pageSize: parseInt(params.pageSize),
        refundStatus: params.refundStatus,
    };
};

export const refundDataRequestParametersSchema = object().shape({
    pageNumber: number().min(1).default(1),
    pageSize: number().min(1).default(DEFAULT_PAGINATION_SIZE),
    refundStatus: string().oneOf(Object.values(RefundStatusOption)).default(RefundStatusOption.open),
});

export type RefundDataRequestParameters = InferType<typeof refundDataRequestParametersSchema>;

export const parseAndValidateRefundDataRequestParameters = (
    refundDataRequestParmatersBody: unknown
): RefundDataRequestParameters => {
    return parseAndValidateStrict(
        parseParameters(refundDataRequestParmatersBody),
        refundDataRequestParametersSchema,
        'Could not parse the refund data request parameters. Unknown Reason.'
    );
};


