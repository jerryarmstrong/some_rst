apps/backend-serverless/__tests__/unit/services/shopify/admin-data.service.test.ts
==================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import { makeAdminData } from '../../../../src/services/shopify/admin-data.service.js';
import { createMockAdminDataResponse } from '../../../../src/utilities/testing-helper/create-mock.utility.js';

describe('unit testing payment app configure', () => {
    it('successful response', async () => {
        const mock = new MockAdapter(axios);
        const mockAdminDataResponse = createMockAdminDataResponse();
        mock.onPost().reply(200, mockAdminDataResponse);
        const mockAdminData = makeAdminData(axios);

        await expect(mockAdminData('mock-shop', 'mock-token')).resolves.not.toThrow();
    });
});


