apps/backend-serverless/src/models/shopify/access-token-response.model.ts
=========================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, object, string } from 'yup';
import { parseAndValidateStrict } from '../../utilities/yup.utility.js';

export const accessTokenResponseSchema = object().shape({
    access_token: string().required(),
    scope: string().required(),
});

export type AccessTokenResponse = InferType<typeof accessTokenResponseSchema>;

export const parseAndValidateAccessTokenResponse = (accessTokenResponseBody: unknown): AccessTokenResponse => {
    return parseAndValidateStrict(
        accessTokenResponseBody,
        accessTokenResponseSchema,
        'Could not parse the access token response. Unknown Reason.',
    );
};


