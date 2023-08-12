tools/analytics/stakedTokensBreakdownByWallet.ts
================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { Wallet } from "@coral-xyz/anchor";
import type { Connection } from "@solana/web3.js";
import { PublicKey } from "@solana/web3.js";
import { BN } from "bn.js";

import { getActiveStakeEntriesForPool } from "../../src/programs/stakePool/accounts";

export const commandName = "stakedTokensBreakdownByWallet";
export const description =
  "Get a breakdown of all staked tokens in a pool by wallet";

export const getArgs = (_connection: Connection, _wallet: Wallet) => ({
  poolId: new PublicKey("3BZCupFU6X3wYJwgTsKS2vTs4VeMrhSZgx4P2TfzExtP"),
});

export const handler = async (
  connection: Connection,
  _wallet: Wallet,
  args: ReturnType<typeof getArgs>
) => {
  const UTCNow = Date.now() / 1000;
  const stakeEntries = await getActiveStakeEntriesForPool(
    connection,
    args.poolId
  );
  const results = stakeEntries.reduce(
    (acc, stakeEntry) => {
      const wallet = stakeEntry.parsed.lastStaker.toString();
      const currentEntry = {
        wallet,
        totalStakeAmount: stakeEntry.parsed.amount.toNumber(),
        totalStakeSeconds: stakeEntry.parsed.totalStakeSeconds
          .add(
            new BN(UTCNow).sub(
              stakeEntry.parsed.lastUpdatedAt ?? stakeEntry.parsed.lastStakedAt
            )
          )
          .toNumber(),
      };
      const existingEntry = acc[wallet];
      if (existingEntry) {
        acc[wallet] = {
          wallet,
          totalStakeAmount:
            existingEntry.totalStakeAmount + currentEntry.totalStakeAmount,
          totalStakeSeconds:
            existingEntry.totalStakeSeconds + currentEntry.totalStakeSeconds,
        };
      } else {
        acc[wallet] = currentEntry;
      }
      return acc;
    },
    {} as {
      [wallet: string]: {
        wallet: string;
        totalStakeAmount: number;
        totalStakeSeconds: number;
      };
    }
  );

  const sortedResults = Object.values(results).sort(
    (a, b) => b.totalStakeSeconds - a.totalStakeSeconds
  );
  console.log(sortedResults);
};


