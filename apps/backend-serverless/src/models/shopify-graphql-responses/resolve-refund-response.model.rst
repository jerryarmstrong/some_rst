apps/backend-serverless/src/models/shopify-graphql-responses/resolve-refund-response.model.ts
=============================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object } from 'yup';
import { parseAndValidateStrict } from '../../utilities/yup.utility.js';
import { sharedRefundResponseRootSchema, shopifyResponseExtensionsSchema } from './shared.model.js';

export const dataRefundSessionResolveSchema = object().shape({
    refundSessionResolve: sharedRefundResponseRootSchema.required(),
});

export const refundSessionResolveResponseSchema = object().shape({
    data: dataRefundSessionResolveSchema.required(),
    extensions: shopifyResponseExtensionsSchema.required(),
});

export type ResolveRefundResponse = InferType<typeof refundSessionResolveResponseSchema>;

export const parseAndValidateResolveRefundResponse = (resolveRefundResponeBody: unknown): ResolveRefundResponse => {
    return parseAndValidateStrict<ResolveRefundResponse>(
        resolveRefundResponeBody,
        refundSessionResolveResponseSchema,
        'Could not parse the resolve refund response body. Unknown Reason.',
    );
};


