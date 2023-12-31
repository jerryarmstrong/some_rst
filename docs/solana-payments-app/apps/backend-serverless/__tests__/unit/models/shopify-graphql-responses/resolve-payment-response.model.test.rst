apps/backend-serverless/__tests__/unit/models/shopify-graphql-responses/resolve-payment-response.model.test.ts
==============================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateResolvePaymentResponse } from '../../../../src/models/shopify-graphql-responses/resolve-payment-response.model.js';
import {
    runEmptyFieldTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';
import { createMockSuccessPaymentSessionResolveResponse } from '../../../../src/utilities/testing-helper/create-mock.utility.js';

describe('unit testing resolve payment response model', () => {
    const validParams = createMockSuccessPaymentSessionResolveResponse();
    const fields = ['data', 'extensions'];

    runValidParameterTest(parseAndValidateResolvePaymentResponse, validParams);
    runMissingFieldTests(parseAndValidateResolvePaymentResponse, validParams, fields);
    runEmptyFieldTests(parseAndValidateResolvePaymentResponse, validParams, fields);
});


