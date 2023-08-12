js/packages/web/src/views/packCreate/transactions/getAddCardToPack.ts
=====================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { addCardToPack } from '@oyster/common';
import { TransactionInstruction } from '@solana/web3.js';

import { GetAddCardToPackParams } from './interface';

export const getAddCardToPack = async ({
  selectedItems,
  packSetKey,
  walletPublicKey,
}: GetAddCardToPackParams): Promise<TransactionInstruction[]> => {
  const addCardsToPack = selectedItems.map(selectedItem => {
    return addCardToPack({
      ...selectedItem,
      packSetKey,
      authority: walletPublicKey.toBase58(),
    });
  });

  return Promise.all(addCardsToPack);
};


