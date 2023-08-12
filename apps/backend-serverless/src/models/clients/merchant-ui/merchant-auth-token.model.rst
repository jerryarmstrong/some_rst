apps/backend-serverless/src/models/clients/merchant-ui/merchant-auth-token.model.ts
===================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, number, object, string } from 'yup';
import { parseAndValidateStrict } from '../../../utilities/yup.utility.js';

export const merchantAuthTokenSchema = object().shape({
    id: string().required(),
    iat: number().required(),
    exp: number().required(),
});

export type MerchantAuthToken = InferType<typeof merchantAuthTokenSchema>;

export const parseAndValidateMerchantAuthToken = (merchantAuthTokenBody: unknown): MerchantAuthToken => {
    return parseAndValidateStrict(
        merchantAuthTokenBody,
        merchantAuthTokenSchema,
        'Could not parse the merchant auth token body. Unknown Reason.',
    );
};


