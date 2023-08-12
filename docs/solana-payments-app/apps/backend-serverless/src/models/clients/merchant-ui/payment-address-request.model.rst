apps/backend-serverless/src/models/clients/merchant-ui/payment-address-request.model.ts
=======================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { InferType, boolean, object, string } from 'yup';
import { parseAndValidate } from '../../../utilities/yup.utility.js';
import { publicKeySchema } from '../../public-key-schema.model.js';

export const merchantUpdateRequestBodySchema = object().shape({
    paymentAddress: publicKeySchema.optional(),
    name: string().optional(),
    acceptedTermsAndConditions: boolean().optional(),
    acceptedPrivacyPolicy: boolean().optional(),
    dismissCompleted: boolean().optional(),
    kybInquiry: string().optional(),
});

export type MerchantUpdateRequest = InferType<typeof merchantUpdateRequestBodySchema>;

export const parseAndValidatePaymentAddressRequestBody = (
    merchantUpdateRequestBody: unknown
): MerchantUpdateRequest => {
    return parseAndValidate(
        merchantUpdateRequestBody,
        merchantUpdateRequestBodySchema,
        'Could not parse the merchant update request body. Unknown Reason.'
    );
};


