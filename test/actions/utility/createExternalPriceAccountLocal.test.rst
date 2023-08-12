test/actions/utility/createExternalPriceAccountLocal.test.ts
============================================================

Last edited: 2022-06-14 09:19:26

Contents:

.. code-block:: ts

    import { generateConnectionAndWallet } from '../shared';
import { createExternalPriceAccount } from '../../../src/actions/utility';

describe('creating an external price account', () => {
  describe('success', () => {
    test('creates EPA', async () => {
      const { connection, wallet } = await generateConnectionAndWallet();

      const externalPriceAccount = await createExternalPriceAccount({
        connection,
        wallet,
      });

      expect(externalPriceAccount).toHaveProperty('externalPriceAccount');
      expect(externalPriceAccount).toHaveProperty('priceMint');
    });
  });
});


