apps/backend-serverless/__tests__/unit/models/step-functions/safety-key-sweep.model.test.ts
===========================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateSafetyKeyMessage } from '../../../../src/models/step-functions/safety-key-sweep.model.js';
import {
    runEmptyFieldTests,
    runInvalidFieldTypeTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing the safety key model', () => {
    const validParams = {
        key: 'some-id',
    };

    const fields = ['key'];

    const wrongTypes = {
        key: 123,
    };

    runValidParameterTest(parseAndValidateSafetyKeyMessage, validParams);
    runMissingFieldTests(parseAndValidateSafetyKeyMessage, validParams, fields);
    runInvalidFieldTypeTests(parseAndValidateSafetyKeyMessage, validParams, fields, wrongTypes);
    runEmptyFieldTests(parseAndValidateSafetyKeyMessage, validParams, fields);
});


