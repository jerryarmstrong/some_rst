apps/backend-serverless/__tests__/unit/models/transaction-requests/transaction-request-body.model.test.ts
=========================================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateTransactionRequestBody } from '../../../../src/models/transaction-requests/transaction-request-body.model.js';
import {
    runEmptyFieldTests,
    runInvalidFieldTypeTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing the transaction request body model', () => {
    const validParams = {
        account: 'some-id',
    };

    const fields = ['account'];

    const wrongTypes = {
        account: 123,
    };

    runValidParameterTest(parseAndValidateTransactionRequestBody, validParams);
    runMissingFieldTests(parseAndValidateTransactionRequestBody, validParams, fields);
    runInvalidFieldTypeTests(parseAndValidateTransactionRequestBody, validParams, fields, wrongTypes);
    runEmptyFieldTests(parseAndValidateTransactionRequestBody, validParams, fields);
});


