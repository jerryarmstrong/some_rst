fixed-price-sale/js/test/actions/createPrerequisites.ts
=======================================================

Last edited: 2023-07-31 23:00:16

Contents:

.. code-block:: ts

    import { Connection, Keypair } from '@solana/web3.js';
import { Amman } from '@metaplex-foundation/amman-client';

import { connectionURL } from '../utils';
import { cusper } from '../../src';

export const createPrerequisites = async () => {
  const payer = Keypair.generate();

  const connection = new Connection(connectionURL, 'confirmed');
  const amman = await Amman.instance({ errorResolver: cusper });
  await amman.airdrop(connection, payer.publicKey, 30);

  return {
    payer,
    connection,
    transactionHandler: amman.payerTransactionHandler(connection, payer),
  };
};


