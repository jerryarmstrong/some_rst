apps/backend-serverless/__tests__/unit/models/shopify-graphql-responses/payment-app-configure-response.model.test.ts
====================================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidatePaymentAppConfigureResponse } from '../../../../src/models/shopify-graphql-responses/payment-app-configure-response.model.js';
import {
    runEmptyFieldTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';
import { createMockPaymentAppConfigureResponse } from '../../../../src/utilities/testing-helper/create-mock.utility.js';

describe('unit testing payment app configure model', () => {
    const validParams = createMockPaymentAppConfigureResponse();

    const fields = ['data', 'extensions'];

    runValidParameterTest(parseAndValidatePaymentAppConfigureResponse, validParams);
    runMissingFieldTests(parseAndValidatePaymentAppConfigureResponse, validParams, fields);
    runEmptyFieldTests(parseAndValidatePaymentAppConfigureResponse, validParams, fields);
});


