js/packages/web/src/views/packCreate/transactions/getCreateTokenAccounts.ts
===========================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { programIds } from '@oyster/common';
import { AccountLayout } from '@solana/spl-token';
import { TransactionInstruction } from '@solana/web3.js';

import { getCreateAccount } from './getCreateAccount';
import { GetCreateTokenAccounts } from './interface';

export const getCreateTokenAccounts = ({
  cardsToAdd,
  connection,
  walletPublicKey,
}: GetCreateTokenAccounts): Promise<TransactionInstruction[]> =>
  Promise.all(
    cardsToAdd.map(({ toAccount }) =>
      getCreateAccount({
        connection,
        walletPublicKey,
        newAccountPubkey: toAccount.publicKey,
        space: AccountLayout.span,
        programId: programIds().token,
      }),
    ),
  );


