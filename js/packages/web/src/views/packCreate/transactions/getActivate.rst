js/packages/web/src/views/packCreate/transactions/getActivate.ts
================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { activate } from '@oyster/common';
import { TransactionInstruction } from '@solana/web3.js';

import { GetActivateParams } from './interface';

export const getActivate = async ({
  packSetKey,
  walletPublicKey,
}: GetActivateParams): Promise<TransactionInstruction> => {
  return activate({
    packSetKey,
    authority: walletPublicKey.toBase58(),
  });
};


