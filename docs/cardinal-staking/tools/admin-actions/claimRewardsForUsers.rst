tools/admin-actions/claimRewardsForUsers.ts
===========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { tryGetAccount } from "@cardinal/common";
import type { Wallet } from "@coral-xyz/anchor";
import type { Connection } from "@solana/web3.js";
import { PublicKey, Transaction } from "@solana/web3.js";

import { executeTransaction } from "../../src";
import { getRewardDistributor } from "../../src/programs/rewardDistributor/accounts";
import { findRewardDistributorId } from "../../src/programs/rewardDistributor/pda";
import { withClaimRewards } from "../../src/programs/rewardDistributor/transaction";
import { getActiveStakeEntriesForPool } from "../../src/programs/stakePool/accounts";
import { withUpdateTotalStakeSeconds } from "../../src/programs/stakePool/transaction";
import { chunkArray } from "../utils";

export const commandName = "claimRewardsForUsers";
export const description =
  "Claim all rewards for users in the given pool (must be pool authority) - Cost 0.002 per token";

export const getArgs = (_connection: Connection, _wallet: Wallet) => ({
  // stake pool id
  stakePoolId: new PublicKey("3BZCupFU6X3wYJwgTsKS2vTs4VeMrhSZgx4P2TfzExtP"),
  // number of entries per transaction
  batchSize: 4,
  // number of transactions in parallel
  parallelTransactions: 5,
});

export const handler = async (
  connection: Connection,
  wallet: Wallet,
  args: ReturnType<typeof getArgs>
) => {
  const { stakePoolId } = args;
  const rewardDistributorId = findRewardDistributorId(stakePoolId);
  const checkRewardDistributorData = await tryGetAccount(() =>
    getRewardDistributor(connection, rewardDistributorId)
  );
  if (!checkRewardDistributorData) {
    throw "No reward distributor found";
  }

  const activeStakeEntries = await getActiveStakeEntriesForPool(
    connection,
    stakePoolId
  );
  console.log(
    `Estimated SOL needed to claim rewards for ${activeStakeEntries.length} staked tokens:`,
    0.002 * activeStakeEntries.length,
    "SOL"
  );

  const chunkedEntries = chunkArray(activeStakeEntries, args.batchSize);
  const batchedChunks = chunkArray(chunkedEntries, args.parallelTransactions);
  for (let i = 0; i < batchedChunks.length; i++) {
    const chunk = batchedChunks[i]!;
    console.log(`> ${i + 1}/ ${batchedChunks.length}`);
    await Promise.all(
      chunk.map(async (entries, index) => {
        const transaction = new Transaction();
        for (let j = 0; j < entries.length; j++) {
          console.log(`>> ${j + 1}/ ${entries.length}`);
          const stakeEntryData = entries[j]!;
          await withUpdateTotalStakeSeconds(transaction, connection, wallet, {
            stakeEntryId: stakeEntryData.pubkey,
            lastStaker: wallet.publicKey,
          });
          await withClaimRewards(transaction, connection, wallet, {
            stakePoolId: stakePoolId,
            stakeEntryId: stakeEntryData.pubkey,
            lastStaker: stakeEntryData.parsed.lastStaker,
            payer: wallet.publicKey,
          });
        }
        try {
          if (transaction.instructions.length > 0) {
            const txid = await executeTransaction(
              connection,
              wallet,
              transaction,
              {}
            );
            console.log(
              `[${index + 1}/${
                chunk.length
              }] [success] Claimed rewards (https://explorer.solana.com/tx/${txid})`
            );
          }
        } catch (e) {
          console.log(e);
        }
      })
    );
  }

  console.log(
    `[success] Claimed rewards for ${activeStakeEntries.length} staked tokens`
  );
};


