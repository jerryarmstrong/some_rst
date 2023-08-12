apps/backend-serverless/__tests__/unit/models/dependencies/helius-header.model.test.ts
======================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { HeliusHeader, parseAndValidateHeliusHeader } from '../../../../src/models/dependencies/helius-header.model.js';
import {
    runEmptyFieldTests,
    runInvalidFieldTypeTests,
    runMissingFieldTests,
    runValidParameterTest,
} from '../../../../src/utilities/testing-helper/common-model-test.utility.js';

describe('unit testing Helius header model', () => {
    const validParams: HeliusHeader = {
        authorization: 'Bearer token',
    };

    const fields = ['authorization'];
    const wrongTypes = {
        authorization: 12345, // should be a string
    };

    runValidParameterTest(parseAndValidateHeliusHeader, validParams);
    runInvalidFieldTypeTests(parseAndValidateHeliusHeader, validParams, fields, wrongTypes);
    runMissingFieldTests(parseAndValidateHeliusHeader, validParams, fields);
    runEmptyFieldTests(parseAndValidateHeliusHeader, validParams, fields);
});


