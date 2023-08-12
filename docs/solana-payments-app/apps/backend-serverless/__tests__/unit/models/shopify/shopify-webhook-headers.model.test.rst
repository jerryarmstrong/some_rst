apps/backend-serverless/__tests__/unit/models/shopify/shopify-webhook-headers.model.test.ts
===========================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateShopifyWebhookHeaders } from '../../../../src/models/shopify/shopify-webhook-headers.model.js';
import {
    runEmptyFieldTests,
    runInvalidFieldTypeTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing shopify webhooks headers model', () => {
    const validParams = {
        'X-Shopify-Topic': 'customers/data_request',
        'X-Shopify-Hmac-Sha256': 'some-hmac',
        'X-Shopify-Shop-Domain': 'some-domain',
        'X-Shopify-API-Version': 'some-api-version',
        'X-Shopify-Webhook-Id': 'some-webhook-id',
        'X-Shopify-Triggered-At': 'some-triggered-at',
    };

    const fields = [
        'X-Shopify-Topic',
        'X-Shopify-Hmac-Sha256',
        'X-Shopify-Shop-Domain',
        'X-Shopify-API-Version',
        'X-Shopify-Webhook-Id',
        'X-Shopify-Triggered-At',
    ];

    const wrongTypes = {
        'X-Shopify-Topic': 123,
        'X-Shopify-Hmac-Sha256': 123,
        'X-Shopify-Shop-Domain': 123,
        'X-Shopify-API-Version': 123,
        'X-Shopify-Webhook-Id': 123,
        'X-Shopify-Triggered-At': 123,
    };

    runValidParameterTest(parseAndValidateShopifyWebhookHeaders, validParams);
    runMissingFieldTests(parseAndValidateShopifyWebhookHeaders, validParams, fields);
    runInvalidFieldTypeTests(parseAndValidateShopifyWebhookHeaders, validParams, fields, wrongTypes);
    runEmptyFieldTests(parseAndValidateShopifyWebhookHeaders, validParams, fields);
});


