src/programs/groupRewardDistributor/utils.ts
============================================

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

import { GroupRewardDistributorKind } from "./constants";

export const withRemainingAccountsForRewardKind = async (
  transaction: Transaction,
  connection: Connection,
  wallet: Wallet,
  groupRewardDistributorId: PublicKey,
  kind: GroupRewardDistributorKind,
  rewardMint: PublicKey,
  isClaimGroupRewards?: boolean
): Promise<AccountMeta[]> => {
  switch (kind) {
    case GroupRewardDistributorKind.Mint: {
      return [];
    }
    case GroupRewardDistributorKind.Treasury: {
      const rewardDistributorGroupRewardMintTokenAccountId =
        await withFindOrInitAssociatedTokenAccount(
          transaction,
          connection,
          rewardMint,
          groupRewardDistributorId,
          wallet.publicKey,
          true
        );
      const userGroupRewardMintTokenAccountId = await findAta(
        rewardMint,
        wallet.publicKey,
        true
      );
      return [
        {
          pubkey: rewardDistributorGroupRewardMintTokenAccountId,
          isSigner: false,
          isWritable: true,
        },
      ].concat(
        !isClaimGroupRewards
          ? [
              {
                pubkey: userGroupRewardMintTokenAccountId,
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


