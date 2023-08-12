tools/admin-actions/updateMultipliersOnRules.ts
===============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { tryGetAccount } from "@cardinal/common";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import type { Connection } from "@solana/web3.js";
import { PublicKey, Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import { executeTransaction } from "../../src";
import {
  getRewardDistributor,
  getRewardEntries,
} from "../../src/programs/rewardDistributor/accounts";
import {
  findRewardDistributorId,
  findRewardEntryId,
} from "../../src/programs/rewardDistributor/pda";
import {
  withInitRewardEntry,
  withUpdateRewardEntry,
} from "../../src/programs/rewardDistributor/transaction";
import {
  getActiveStakeEntriesForPool,
  getStakeEntries,
} from "../../src/programs/stakePool/accounts";
import { findStakeEntryId } from "../../src/programs/stakePool/pda";
import { fetchMetadata } from "../metadata";

export const commandName = "updateMultipliersOnRules";
export const description = `Update reward multipliers for mints based on traits or other rules. (must be pool authority)
Rules options:
  volume - (if user stakes 2+ token, set token multpliers to 'X', if user staked 5+ token, set token multiplier to 'Y')
  metadata - (if token has metadata attribute equal to specify value, set 'X' multiplier)
  combination - (if user has to stake A,B,C mints together, token get 'X' multiplier, else set to zero)`;

export const getArgs = (_connection: Connection, _wallet: Wallet) => ({
  stakePoolId: new PublicKey("3BZCupFU6X3wYJwgTsKS2vTs4VeMrhSZgx4P2TfzExtP"),
  updateRules: [
    // {
    //   volume: [
    //     { volumeUpperBound: 1, multiplier: 1 },
    //     { volumeUpperBound: 4, multiplier: 3 },
    //     { volumeUpperBound: 7, multiplier: 6 },
    //     { volumeUpperBound: 9, multiplier: 7 },
    //     { volumeUpperBound: 15, multiplier: 10 },
    //     { volumeUpperBound: 29, multiplier: 20 },
    //     { volumeUpperBound: 39, multiplier: 25 },
    //     { volumeUpperBound: 40, multiplier: 30 },
    //   ],
    // },
    // {
    // metadata: [{ traitType: "some_trait", value: "value", multiplier: 2 }],
    // },
  ] as UpdateRule[],
  batchSize: 5,
});

export type UpdateRule = {
  volume?: { volumeUpperBound: number; multiplier: number }[];
  metadata?: { traitType: string; value: string; multiplier: number }[];
  combination?: {
    primaryMint: PublicKey[];
    secondaryMints: PublicKey[];
    multiplier: number;
  };
};

export const handler = async (
  connection: Connection,
  wallet: Wallet,
  args: ReturnType<typeof getArgs>
) => {
  const { stakePoolId, updateRules, batchSize } = args;
  const activeStakeEntries = await getActiveStakeEntriesForPool(
    connection,
    stakePoolId
  );

  for (const rule of updateRules) {
    let dataToSubmit: { mint: PublicKey; multiplier: number }[] = [];

    //////////////////////// metadata ////////////////////////
    if (rule.metadata) {
      console.log("Fetching metadata...");
      const [metadata] = await fetchMetadata(
        connection,
        activeStakeEntries.map((entry) => entry.parsed.originalMint)
      );
      console.log("Constructing multipliers...");
      const metadataLogs: { [multiplier: number]: PublicKey[] } = {};
      for (let index = 0; index < metadata.length; index++) {
        const md = metadata[index]!;
        for (const mdRule of rule.metadata) {
          if (
            md.attributes.find(
              (attr) =>
                attr.trait_type === mdRule.traitType &&
                attr.value === mdRule.value
            )
          ) {
            if (metadataLogs[mdRule.multiplier]) {
              metadataLogs[mdRule.multiplier]!.push(
                activeStakeEntries[index]!.pubkey
              );
            } else {
              metadataLogs[mdRule.multiplier] = [
                activeStakeEntries[index]!.pubkey,
              ];
            }
          }
        }
      }

      // Update multiplier of mints
      for (const [multiplierToSet, entries] of Object.entries(metadataLogs)) {
        if (entries.length > 0) {
          for (let index = 0; index < entries.length; index++) {
            const entry = entries[index]!;
            dataToSubmit.push({
              mint: entry,
              multiplier: Number(multiplierToSet),
            });
            if (
              dataToSubmit.length > batchSize ||
              index === entries.length - 1
            ) {
              await updateMultipliers(
                connection,
                wallet,
                stakePoolId,
                dataToSubmit.map((entry) => entry.mint),
                dataToSubmit.map((entry) => entry.multiplier)
              );
              dataToSubmit = [];
            }
          }
        }
      }
    } else if (rule.volume) {
      //////////////////////// volume ////////////////////////
      const volumeLogs: { [user: string]: PublicKey[] } = {};
      for (const entry of activeStakeEntries) {
        const user = entry.parsed.lastStaker.toString();
        if (volumeLogs[user]) {
          volumeLogs[user]!.push(entry.pubkey);
        } else {
          volumeLogs[user] = [entry.pubkey];
        }
      }
      for (const [_, entries] of Object.entries(volumeLogs)) {
        if (entries.length > 0) {
          // find multiplier for volume
          const volume = entries.length;
          let multiplierToSet = 1;
          for (const volumeRule of rule.volume) {
            multiplierToSet = volumeRule.multiplier;
            if (volume <= volumeRule.volumeUpperBound) {
              break;
            }
          }

          // Update multiplier of mints
          for (const entry of entries) {
            dataToSubmit.push({
              mint: entry,
              multiplier: multiplierToSet,
            });
            if (dataToSubmit.length > batchSize) {
              await updateMultipliers(
                connection,
                wallet,
                stakePoolId,
                dataToSubmit.map((entry) => entry.mint),
                dataToSubmit.map((entry) => entry.multiplier)
              );
              dataToSubmit = [];
            }
          }
        }
      }
    } else if (rule.combination) {
      //////////////////////// combinations ////////////////////////
      const primaryMints = rule.combination.primaryMint;
      const secondaryMints = rule.combination.secondaryMints;
      const combinationLogs: { [user: string]: string[] } = {};

      for (const entry of activeStakeEntries) {
        const user = entry.parsed.lastStaker.toString();
        if (combinationLogs[user]) {
          combinationLogs[user]!.push(entry.pubkey.toString());
        } else {
          combinationLogs[user] = [entry.pubkey.toString()];
        }
      }
      for (const [_, entries] of Object.entries(combinationLogs)) {
        let multiplierToSet = 0;
        let validCombination = true;
        // Calculate if multiplier for primary mints
        for (const mint of primaryMints) {
          if (!entries.includes(mint.toString())) {
            validCombination = false;
            break;
          }
        }
        for (const mint of secondaryMints) {
          if (!entries.includes(mint.toString()) || !validCombination) {
            validCombination = false;
            break;
          }
        }

        if (validCombination) {
          multiplierToSet = rule.combination.multiplier;
        }

        // Update multiplier of primary mints
        for (const primaryMint of primaryMints) {
          const stakeEntryId = findStakeEntryId(
            wallet.publicKey,
            stakePoolId,
            primaryMint,
            false
          );
          dataToSubmit.push({
            mint: stakeEntryId,
            multiplier: multiplierToSet,
          });
          if (dataToSubmit.length > batchSize) {
            await updateMultipliers(
              connection,
              wallet,
              stakePoolId,
              dataToSubmit.map((entry) => entry.mint),
              dataToSubmit.map((entry) => entry.multiplier)
            );
            dataToSubmit = [];
          }
        }
      }
    }
  }
};

const updateMultipliers = async (
  connection: Connection,
  wallet: Wallet,
  stakePoolId: PublicKey,
  stakeEntryIds: PublicKey[],
  multipliers: number[]
): Promise<void> => {
  const transaction = new Transaction();
  // update multipliers
  const rewardDistributorId = findRewardDistributorId(stakePoolId);
  const rewardDistributorData = await tryGetAccount(() =>
    getRewardDistributor(connection, rewardDistributorId)
  );
  if (!rewardDistributorData) {
    console.log("No reward distributor found");
    return;
  }

  const multipliersToSet = multipliers.map(
    (ml) => ml * 10 ** rewardDistributorData.parsed.multiplierDecimals
  );

  const rewardEntryIds = stakeEntryIds.map((stakeEntryId) =>
    findRewardEntryId(rewardDistributorId, stakeEntryId)
  );
  const stakeEntryDatas = await getStakeEntries(connection, stakeEntryIds);
  const rewardEntryDatas = await getRewardEntries(connection, rewardEntryIds);
  // Add init reward entry instructions
  await Promise.all(
    rewardEntryDatas.map((rewardEntryData, index) => {
      if (!rewardEntryData.parsed) {
        const stakeEntryId = stakeEntryIds[index]!;
        return withInitRewardEntry(transaction, connection, wallet, {
          stakeEntryId: stakeEntryId,
          rewardDistributorId: rewardDistributorId,
        });
      }
    })
  );

  // Add update instruction if needed
  await Promise.all(
    rewardEntryDatas.map((rewardEntryData, index) => {
      const multiplierToSet = multipliersToSet[index]!;
      const stakeEntryId = stakeEntryIds[index]!;
      if (
        !rewardEntryData.parsed ||
        (rewardEntryData.parsed &&
          rewardEntryData.parsed.multiplier.toNumber() !== multiplierToSet)
      ) {
        console.log(
          `Updating multiplier for mint ${stakeEntryDatas[
            index
          ]!.parsed.originalMint.toString()} from ${
            rewardEntryData.parsed
              ? rewardEntryData.parsed.multiplier.toString()
              : "100"
          } to ${multiplierToSet}`
        );
        return withUpdateRewardEntry(transaction, connection, wallet, {
          stakePoolId: stakePoolId,
          rewardDistributorId: rewardDistributorId,
          stakeEntryId: stakeEntryId,
          multiplier: new BN(multiplierToSet),
        });
      }
    })
  );

  // Execute transaction
  if (transaction.instructions.length > 0) {
    const txId = await executeTransaction(connection, wallet, transaction, {});
    console.log(`Successfully executed transaction ${txId}\n`);
  } else {
    console.log("No instructions provided\n");
  }
};


