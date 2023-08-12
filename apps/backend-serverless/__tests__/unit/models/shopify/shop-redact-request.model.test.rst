apps/backend-serverless/__tests__/unit/models/shopify/shop-redact-request.model.test.ts
=======================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateShopRedactRequestBody } from '../../../../src/models/shopify/shop-redact-request.model.js';
import {
    runEmptyFieldTests,
    runInvalidFieldTypeTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing shop redact request model', () => {
    const validParams = {
        shop_id: '123456',
        shop_domain: 'some-shop.myshopify.com',
    };
    const fields = ['shop_id', 'shop_domain'];
    const wrongTypes = {
        shop_id: 123,
        shop_domain: 123,
    };

    runValidParameterTest(parseAndValidateShopRedactRequestBody, validParams);
    runMissingFieldTests(parseAndValidateShopRedactRequestBody, validParams, fields);
    runInvalidFieldTypeTests(parseAndValidateShopRedactRequestBody, validParams, fields, wrongTypes);
    runEmptyFieldTests(parseAndValidateShopRedactRequestBody, validParams, fields);
});


