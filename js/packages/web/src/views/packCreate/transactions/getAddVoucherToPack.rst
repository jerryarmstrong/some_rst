js/packages/web/src/views/packCreate/transactions/getAddVoucherToPack.ts
========================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { addVoucherToPack } from '@oyster/common';
import { TransactionInstruction } from '@solana/web3.js';

import { GetAddVoucherToPackParams } from './interface';

export const getAddVoucherToPack = async ({
  selectedVouchers,
  packSetKey,
  walletPublicKey,
}: GetAddVoucherToPackParams): Promise<TransactionInstruction[]> => {
  const addVouchersToPack = selectedVouchers.map(voucher => {
    return addVoucherToPack({
      ...voucher,
      packSetKey,
      authority: walletPublicKey.toBase58(),
    });
  });

  return Promise.all(addVouchersToPack);
};


