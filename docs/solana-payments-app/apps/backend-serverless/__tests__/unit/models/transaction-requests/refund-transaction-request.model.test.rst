apps/backend-serverless/__tests__/unit/models/transaction-requests/refund-transaction-request.model.test.ts
===========================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateRefundTransactionRequest } from '../../../../src/models/transaction-requests/refund-transaction-request.model.js';
import {
    runEmptyFieldTests,
    runInvalidFieldTypeTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing the refund transaction request model', () => {
    const validParams = {
        refundId: 'some-id',
    };

    const fields = ['refundId'];

    const wrongTypes = {
        refundId: 123,
    };

    runValidParameterTest(parseAndValidateRefundTransactionRequest, validParams);
    runMissingFieldTests(parseAndValidateRefundTransactionRequest, validParams, fields);
    runInvalidFieldTypeTests(parseAndValidateRefundTransactionRequest, validParams, fields, wrongTypes);
    runEmptyFieldTests(parseAndValidateRefundTransactionRequest, validParams, fields);
});


