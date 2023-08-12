apps/backend-serverless/__tests__/unit/models/shopify-graphql-responses/resolve-refund-response.model.test.ts
=============================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateResolveRefundResponse } from '../../../../src/models/shopify-graphql-responses/resolve-refund-response.model.js';
import { createMockSuccessRefundSessionResolveResponse } from '../../../../src/utilities/testing-helper/create-mock.utility.js';

import {
    runEmptyFieldTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing resolve refund response model', () => {
    const validParams = createMockSuccessRefundSessionResolveResponse();
    const fields = ['data', 'extensions'];

    runValidParameterTest(parseAndValidateResolveRefundResponse, validParams);
    runMissingFieldTests(parseAndValidateResolveRefundResponse, validParams, fields);
    runEmptyFieldTests(parseAndValidateResolveRefundResponse, validParams, fields);
});


