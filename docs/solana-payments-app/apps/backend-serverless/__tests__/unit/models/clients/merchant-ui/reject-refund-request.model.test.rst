apps/backend-serverless/__tests__/unit/models/clients/merchant-ui/reject-refund-request.model.test.ts
=====================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateRejectRefundRequest } from '../../../../../src/models/clients/merchant-ui/reject-refund-request.model.js';
import {
    runEmptyFieldTests,
    runInvalidFieldTypeTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing reject refund request model', () => {
    const fields = ['refundId', 'merchantReason'];
    const validParams = {
        refundId: 'test-refund-id',
        merchantReason: 'test-reason',
    };

    const wrongTypes = {
        refundId: 12345, // should be a string
        merchantReason: 12345, // should be a string
    };

    runValidParameterTest(parseAndValidateRejectRefundRequest, validParams);
    runMissingFieldTests(parseAndValidateRejectRefundRequest, validParams, fields);
    runInvalidFieldTypeTests(parseAndValidateRejectRefundRequest, validParams, fields, wrongTypes);
    runEmptyFieldTests(parseAndValidateRejectRefundRequest, validParams, fields);
});


