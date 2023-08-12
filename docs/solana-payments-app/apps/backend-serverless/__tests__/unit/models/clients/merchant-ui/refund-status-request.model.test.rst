apps/backend-serverless/__tests__/unit/models/clients/merchant-ui/refund-status-request.model.test.ts
=====================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateRefundStatusRequest } from '../../../../../src/models/clients/merchant-ui/refund-status-request.model.js';
import {
    runEmptyFieldTests,
    runInvalidFieldTypeTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing refund status request model', () => {
    const fields = ['shopId'];
    const validParams = {
        shopId: 'test-shop-id',
    };

    const wrongTypes = {
        shopId: 12345, // should be a string
    };

    runValidParameterTest(parseAndValidateRefundStatusRequest, validParams);
    runMissingFieldTests(parseAndValidateRefundStatusRequest, validParams, fields);
    runInvalidFieldTypeTests(parseAndValidateRefundStatusRequest, validParams, fields, wrongTypes);
    runEmptyFieldTests(parseAndValidateRefundStatusRequest, validParams, fields);
});


