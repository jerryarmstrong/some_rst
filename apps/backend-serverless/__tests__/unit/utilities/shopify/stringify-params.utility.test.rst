apps/backend-serverless/__tests__/unit/utilities/shopify/stringify-params.utility.test.ts
=========================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { parseAndValidateAppInstallQueryParms } from '../../../../src/models/shopify/install-query-params.model.js';
import { stringifyParams } from '../../../../src/utilities/shopify/stringify-params.utility.js';

describe('stringifyParams', () => {
    it('should return a string', () => {
        const validInstallQueryParams = {
            hmac: 'some-hmac',
            shop: 'https://some-shop.myshopify.com',
            host: 'some-host',
            timestamp: 'some-timestamp',
        };

        const installParams = parseAndValidateAppInstallQueryParms(validInstallQueryParams);

        const result = stringifyParams(installParams);

        const expectedResult =
            'hmac=some-hmac&shop=https://some-shop.myshopify.com&host=some-host&timestamp=some-timestamp';

        expect(result).toBe(expectedResult);
    });
});


