apps/backend-serverless/__tests__/unit/models/shopify-graphql-responses/reject-refund-response.model.test.ts
============================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateRejectRefundResponse } from '../../../../src/models/shopify-graphql-responses/reject-refund-response.model.js';
import {
    runEmptyFieldTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';
import { createMockSuccessRefundSessionRejectResponse } from '../../../../src/utilities/testing-helper/create-mock.utility.js';

describe('unit testing reject refund response model', () => {
    const validParams = createMockSuccessRefundSessionRejectResponse();
    const fields = ['data', 'extensions'];

    runValidParameterTest(parseAndValidateRejectRefundResponse, validParams);
    runMissingFieldTests(parseAndValidateRejectRefundResponse, validParams, fields);
    runEmptyFieldTests(parseAndValidateRejectRefundResponse, validParams, fields);
});


