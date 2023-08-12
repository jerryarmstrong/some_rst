token-vault/js/src/common/account-setup.ts
==========================================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    import { Connection, Keypair, PublicKey } from '@solana/web3.js';
import { InstructionsWithAccounts } from '../types';
import { createTokenAccount, getTokenRentExempt } from './helpers';

export async function setupDestinationTokenAccount(
  connection: Connection,
  args: {
    payer: PublicKey;
    mint: PublicKey;
  },
): Promise<InstructionsWithAccounts<{ destination: PublicKey; destinationPair: Keypair }>> {
  const rentExempt = await getTokenRentExempt(connection);
  const { payer, mint } = args;
  const [instructions, signers, { tokenAccount: destination, tokenAccountPair: destinationPair }] =
    createTokenAccount(payer, rentExempt, mint, payer);
  return [instructions, signers, { destination, destinationPair }];
}


