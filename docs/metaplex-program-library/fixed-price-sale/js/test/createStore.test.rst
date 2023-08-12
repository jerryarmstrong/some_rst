fixed-price-sale/js/test/createStore.test.ts
============================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    import test from 'tape';

import { killStuckProcess } from './utils';
import { createStore, createPrerequisites } from './actions';

killStuckProcess();

test('create-store: success', async (t) => {
  const { payer, connection, transactionHandler } = await createPrerequisites();

  await createStore({
    test: t,
    transactionHandler,
    payer,
    connection,
    params: {
      name: 'Store',
      description: 'Description',
    },
  });
});

test('create-store: short name and empty description', async (t) => {
  const { payer, connection, transactionHandler } = await createPrerequisites();

  await createStore({
    test: t,
    transactionHandler,
    payer,
    connection,
    params: {
      name: 'Store',
      description: '',
    },
  });
});


