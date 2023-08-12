js/packages/web/src/views/packCreate/transactions/getCreateAccount.ts
=====================================================================

Last edited: 2022-06-29 06:18:54

Contents:

.. code-block:: ts

    import { SystemProgram, TransactionInstruction } from '@solana/web3.js';
import { GetCreateAccountParams } from './interface';

export const getCreateAccount = async ({
  connection,
  newAccountPubkey,
  walletPublicKey,
  space,
  programId,
}: GetCreateAccountParams): Promise<TransactionInstruction> => {
  const packSetRentExempt = await connection.getMinimumBalanceForRentExemption(
    space,
  );

  return SystemProgram.createAccount({
    fromPubkey: walletPublicKey,
    newAccountPubkey,
    lamports: packSetRentExempt,
    space,
    programId,
  });
};


