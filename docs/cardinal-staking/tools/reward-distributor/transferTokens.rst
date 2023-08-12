tools/reward-distributor/transferTokens.ts
==========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { withFindOrInitAssociatedTokenAccount } from "@cardinal/common";
import type { Wallet } from "@coral-xyz/anchor";
import {
  createTransferCheckedInstruction,
  getAssociatedTokenAddressSync,
} from "@solana/spl-token";
import type { Connection } from "@solana/web3.js";
import { PublicKey, Transaction } from "@solana/web3.js";

import { executeTransaction } from "../../src";

export const commandName = "transferTokens";
export const description = "Add tokens to reward distributor";

export const getArgs = (_connection: Connection, _wallet: Wallet) => ({
  mint: new PublicKey(""),
  rewardDistributorId: new PublicKey(""),
  amount: 0,
  decimals: 0,
});

export const handler = async (
  connection: Connection,
  wallet: Wallet,
  args: ReturnType<typeof getArgs>
) => {
  const { mint, rewardDistributorId, amount, decimals } = args;
  const ownerAtaId = getAssociatedTokenAddressSync(
    mint,
    wallet.publicKey,
    true
  );

  const transaction = new Transaction();
  const rewardDistributorAtaId = await withFindOrInitAssociatedTokenAccount(
    transaction,
    connection,
    mint,
    rewardDistributorId,
    wallet.publicKey,
    true
  );

  transaction.add(
    createTransferCheckedInstruction(
      ownerAtaId,
      mint,
      rewardDistributorAtaId,
      wallet.publicKey,
      amount,
      decimals
    )
  );

  const txid = await executeTransaction(connection, wallet, transaction, {});
  console.log(`[success] https://explorer.solana.com/tx/${txid}`);
};


