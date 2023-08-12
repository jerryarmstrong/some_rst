apps/backend-serverless/__tests__/unit/models/shopify-graphql-responses/admin-data-response.model.test.ts
=========================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateAdminDataResponse } from '../../../../src/models/shopify-graphql-responses/admin-data.response.model.js';
import { createMockAdminDataResponse } from '../../../../src/utilities/testing-helper/create-mock.utility.js';

import {
    runEmptyFieldTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing payment app configure model', () => {
    const validParams = createMockAdminDataResponse();

    const fields = ['data', 'extensions'];

    runValidParameterTest(parseAndValidateAdminDataResponse, validParams);
    runMissingFieldTests(parseAndValidateAdminDataResponse, validParams, fields);
    runEmptyFieldTests(parseAndValidateAdminDataResponse, validParams, fields);
});


