apps/backend-serverless/__tests__/unit/models/shopify-graphql-responses/reject-payment-response.model.test.ts
=============================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateRejectPaymentResponse } from '../../../../src/models/shopify-graphql-responses/reject-payment-response.model.js';
import {
    runEmptyFieldTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';
import { createMockSuccessPaymentSessionRejectResponse } from '../../../../src/utilities/testing-helper/create-mock.utility.js';

describe('unit testing reject payment response model', () => {
    const validParams = createMockSuccessPaymentSessionRejectResponse();
    const fields = ['data', 'extensions'];

    runValidParameterTest(parseAndValidateRejectPaymentResponse, validParams);
    runMissingFieldTests(parseAndValidateRejectPaymentResponse, validParams, fields);
    runEmptyFieldTests(parseAndValidateRejectPaymentResponse, validParams, fields);
});


