src/programs/rewardDistributor/utils.ts
=======================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import {
  findAta,
  withFindOrInitAssociatedTokenAccount,
} from "@cardinal/common";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import type {
  AccountMeta,
  Connection,
  PublicKey,
  Transaction,
} from "@solana/web3.js";

import { RewardDistributorKind } from "./constants";

export const withRemainingAccountsForKind = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  rewardDistributorId: PublicKey,
  kind: RewardDistributorKind,
  rewardMint: PublicKey,
  isClaimRewards?: boolean
): Promise<AccountMeta[]> => {
  switch (kind) {
    case RewardDistributorKind.Mint: {
      return [];
    }
    case RewardDistributorKind.Treasury: {
      const rewardDistributorRewardMintTokenAccountId =
        await withFindOrInitAssociatedTokenAccount(
          transaction,
          connection,
          rewardMint,
          rewardDistributorId,
          wallet.publicKey,
          true
        );
      const userRewardMintTokenAccountId = await findAta(
        rewardMint,
        wallet.publicKey,
        true
      );
      return [
        {
          pubkey: rewardDistributorRewardMintTokenAccountId,
          isSigner: false,
          isWritable: true,
        },
      ].concat(
        !isClaimRewards
          ? [
              {
                pubkey: userRewardMintTokenAccountId,
                isSigner: false,
                isWritable: true,
              },
            ]
          : []
      );
    }
    default:
      return [];
  }
};


