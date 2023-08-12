tools/admin-actions/initializeEntriesAndSetMultipliers.ts
=========================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { AccountData } from "@cardinal/common";
import { withFindOrInitAssociatedTokenAccount } from "@cardinal/common";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import type { Connection } from "@solana/web3.js";
import { PublicKey, Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import { executeTransaction } from "../../src";
import type { RewardEntryData } from "../../src/programs/rewardDistributor";
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
import type { StakeEntryData } from "../../src/programs/stakePool";
import { getStakeEntries } from "../../src/programs/stakePool/accounts";
import { findStakeEntryId } from "../../src/programs/stakePool/pda";
import { withInitStakeEntry } from "../../src/programs/stakePool/transaction";
import type { MetadataJSON } from "../metadata";
import { fetchMetadata } from "../metadata";
import { chunkArray } from "../utils";
import type { UpdateRule } from "./updateMultipliersOnRules";

export const commandName = "initializeEntriesAndSetMultipliers";
export const description =
  "Initialize all entries and optionally set multipliers for reward entries. Optionalls use metadataRules for complex multiplier rules";

export const getArgs = (_connection: Connection, _wallet: Wallet) => ({
  // stake pool id
  stakePoolId: new PublicKey("3BZCupFU6X3wYJwgTsKS2vTs4VeMrhSZgx4P2TfzExtP"),
  // whether this pool deals with fungible tokens
  fungible: false,
  // array of mints and optionally multiplier to initialize
  // REMINDER: Take into account rewardDistributor.multiplierDecimals!
  initEntries: [] as EntryData[],
  // optional update rules
  metadataRules: undefined as UpdateRule["metadata"],
  // number of entries per transaction
  batchSize: 3,
  // number of transactions in parallel
  parallelBatchSize: 20,
});

type EntryData = { mintId: PublicKey; multiplier?: number };

export const handler = async (
  connection: Connection,
  wallet: Wallet,
  args: ReturnType<typeof getArgs>
) => {
  const { stakePoolId, initEntries, fungible, metadataRules } = args;
  const rewardDistributorId = findRewardDistributorId(stakePoolId);
  const rewardDistributorData = await getRewardDistributor(
    connection,
    rewardDistributorId
  );
  console.log(
    `--------- Initialize ${
      initEntries.length
    } entries for pool (${stakePoolId.toString()}) and reward distributor (${rewardDistributorId.toString()}) ---------`
  );
  const stakeEntryIds = await Promise.all(
    initEntries.map((e) =>
      findStakeEntryId(wallet.publicKey, stakePoolId, e.mintId, fungible)
    )
  );
  const stakeEntries = await getStakeEntries(connection, stakeEntryIds);
  const stakeEntriesById = stakeEntries.reduce(
    (acc, stakeEntry) =>
      stakeEntry.parsed
        ? { ...acc, [stakeEntry.pubkey.toString()]: stakeEntry }
        : { ...acc },
    {} as { [id: string]: AccountData<StakeEntryData> }
  );

  const rewardEntryIds = stakeEntryIds.map((stakeEntryId) =>
    findRewardEntryId(rewardDistributorId, stakeEntryId)
  );
  const rewardEntries = await getRewardEntries(connection, rewardEntryIds);
  const rewardEntriesById = rewardEntries.reduce(
    (acc, rewardEntry) =>
      rewardEntry.parsed
        ? { ...acc, [rewardEntry.pubkey.toString()]: rewardEntry }
        : { ...acc },
    {} as { [id: string]: AccountData<RewardEntryData> }
  );

  const chunkedEntries = chunkArray(initEntries, args.batchSize);
  const batchedChunks = chunkArray(chunkedEntries, args.parallelBatchSize);
  for (let i = 0; i < batchedChunks.length; i++) {
    const chunk = batchedChunks[i]!;
    console.log(`\n\n\n ${i + 1}/${batchedChunks.length}`);
    await Promise.all(
      chunk.map(async (entries, c) => {
        const transaction = new Transaction();
        const entriesInTx: EntryData[] = [];

        let metadata: MetadataJSON[] = [];
        if (metadataRules) {
          [metadata] = await fetchMetadata(
            connection,
            entries.map((e) => e.mintId)
          );
        }
        for (let j = 0; j < entries.length; j++) {
          const { mintId, multiplier } = entries[j]!;
          console.log(
            `>>[${c + 1}/${chunk.length}][${j + 1}/${
              entries.length
            }] (${mintId.toString()})`
          );
          try {
            const stakeEntryId = findStakeEntryId(
              wallet.publicKey,
              stakePoolId,
              mintId,
              fungible
            );

            await withFindOrInitAssociatedTokenAccount(
              transaction,
              connection,
              mintId,
              stakeEntryId,
              wallet.publicKey,
              true
            );

            if (!stakeEntriesById[stakeEntryId.toString()]) {
              await withInitStakeEntry(transaction, connection, wallet, {
                stakePoolId,
                originalMintId: mintId,
                stakeEntryId,
              });
              console.log(
                `>>[${c + 1}/${chunk.length}][${j + 1}/${
                  entries.length
                }] 1. Adding stake entry instruction`
              );
            }

            const rewardEntryId = findRewardEntryId(
              rewardDistributorId,
              stakeEntryId
            );
            const rewardEntry = rewardEntriesById[rewardEntryId.toString()];
            if (rewardDistributorData && !rewardEntry) {
              console.log(
                `>>[${c + 1}/${chunk.length}][${j + 1}/${
                  entries.length
                }] 2. Reward entry not found for reward distributor - adding reward entry instruction`
              );
              await withInitRewardEntry(transaction, connection, wallet, {
                stakeEntryId,
                rewardDistributorId,
              });
            }

            let multiplierToSet = multiplier;
            if (metadataRules) {
              `>>[${c + 1}/${chunk.length}][${j + 1}/${
                entries.length
              }] 2.5 Metadata rules are set to override mint multiplier`;
              const md = metadata[j]!;
              for (const rule of metadataRules) {
                if (
                  md.attributes.find(
                    (attr) =>
                      attr.trait_type === rule.traitType &&
                      attr.value === rule.value
                  )
                ) {
                  multiplierToSet = rule.multiplier;
                  console.log(
                    `>>> [${c + 1}/${chunk.length}][${j + 1}/${
                      entries.length
                    }] Using metadataRule (${rule.traitType}:${rule.value}=${
                      rule.multiplier
                    })`
                  );
                }
              }
            }

            if (
              multiplierToSet &&
              rewardEntry?.parsed.multiplier.toNumber() !== multiplierToSet
            ) {
              console.log(
                `>>[${c + 1}/${chunk.length}][${j + 1}/${
                  entries.length
                }] 3. Updating reward entry multipler from  ${
                  rewardEntry?.parsed.multiplier.toNumber() || 0
                } => ${multiplierToSet}`
              );
              await withUpdateRewardEntry(transaction, connection, wallet, {
                stakePoolId,
                stakeEntryId,
                rewardDistributorId,
                multiplier: new BN(multiplierToSet),
              });
            }
            entriesInTx.push({ mintId });
          } catch (e: unknown) {
            console.log(`[fail] (${mintId.toString()})`);
          }
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
              `[success] ${entriesInTx
                .map((e) => e.mintId.toString())
                .join()} (https://explorer.solana.com/tx/${txid})`
            );
          }
        } catch (e) {
          console.log(e);
        }
      })
    );
  }
};


