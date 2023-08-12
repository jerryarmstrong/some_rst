fixed-price-sale/js/test/initSellingResource.test.ts
====================================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    import test from 'tape';

import { killStuckProcess } from './utils';
import { createPrerequisites, createStore, initSellingResource } from './actions';

killStuckProcess();

test('init-selling-resource: success', async (t) => {
  const { payer, connection, transactionHandler } = await createPrerequisites();

  const store = await createStore({
    test: t,
    transactionHandler,
    payer,
    connection,
    params: {
      name: 'Store',
      description: 'Description',
    },
  });

  await initSellingResource({
    test: t,
    transactionHandler,
    payer,
    connection,
    store: store.publicKey,
    maxSupply: 100,
  });
});


