apps/mock-shopify-serverless/src/models/authorize.models.ts
===========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object, string } from 'yup';
import { parseAndValidate } from '../utilities/yup.utilities.js';

export const authorizeSchema = object().shape({
    client_id: string().required(),
    scope: string().required(),
    redirect_uri: string().required(),
    state: string().required(),
});

export type AuthorizeSchema = InferType<typeof authorizeSchema>;

export const parseAndValidateRejectPaymentResponse = (authorizeParameters: any): AuthorizeSchema => {
    return parseAndValidate(
        authorizeParameters,
        authorizeSchema,
        'Could not parse the authorize parameters. Unknown Reason.',
    );
};


