apps/backend-serverless/src/models/shopify/shop-redact-request.model.ts
=======================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, number, object, string } from 'yup';
import { parseAndValidateStrict } from '../../utilities/yup.utility.js';

export const shopRedactRequestScheme = object().shape({
    shop_id: number().required(),
    shop_domain: string().required(),
});

export type ShopRedactRequest = InferType<typeof shopRedactRequestScheme>;

export const parseAndValidateShopRedactRequestBody = (shopRedactRequestBody: unknown): ShopRedactRequest => {
    return parseAndValidateStrict<ShopRedactRequest>(
        shopRedactRequestBody,
        shopRedactRequestScheme,
        'Could not parse the shop redact body. Unknown Reason.',
    );
};


