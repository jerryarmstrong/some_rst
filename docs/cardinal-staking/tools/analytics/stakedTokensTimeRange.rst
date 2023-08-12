tools/analytics/stakedTokensTimeRange.ts
========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { getProgramIdlAccounts } from "@cardinal/common";
import type { Wallet } from "@coral-xyz/anchor";
import type { Connection } from "@solana/web3.js";
import { PublicKey } from "@solana/web3.js";

import type { STAKE_POOL_PROGRAM } from "../../src/programs/stakePool";
import {
  POOL_OFFSET,
  STAKE_POOL_ADDRESS,
  STAKE_POOL_IDL,
} from "../../src/programs/stakePool";

export const commandName = "stakedTokensTimeRange";
export const description = "Get a snapshot of staked tokens at a timestamp";

export const getArgs = (_connection: Connection, _wallet: Wallet) => ({
  poolId: new PublicKey("BeT8h9E5BcgcMBxF7Si5GSRuB6zHcSpFuMpp6uTcVRFN"),
  startTimestamp: 1671840000,
  activeTimestamp: 1675468800,
});

export const handler = async (
  connection: Connection,
  _wallet: Wallet,
  args: ReturnType<typeof getArgs>
) => {
  const accountInfos = await getProgramIdlAccounts<
    "stakeEntry",
    STAKE_POOL_PROGRAM
  >(connection, "stakeEntry", STAKE_POOL_ADDRESS, STAKE_POOL_IDL, {
    filters: [
      {
        memcmp: { offset: POOL_OFFSET, bytes: args.poolId.toBase58() },
      },
    ],
  });
  const stakeEntries = accountInfos.filter((v) => !!v.parsed);
  const rows = stakeEntries.map((e) => {
    if (!e.parsed) {
      console.log("Failed to deser");
      return "";
    }
    const activeSeconds =
      e.parsed.lastStaker.toString() !== PublicKey.default.toString()
        ? args.activeTimestamp -
          (e.parsed.lastUpdatedAt?.toNumber() ??
            e.parsed.lastStakedAt.toNumber())
        : 0;
    const totalActiveStakeSeconds =
      e.parsed.totalStakeSeconds.toNumber() + activeSeconds;
    return `${e.parsed.originalMint.toString()},${e.parsed.lastStaker.toString()},${e.parsed.totalStakeSeconds.toString()},${e.parsed.lastStakedAt.toString()},${
      e.parsed.lastUpdatedAt?.toString() ?? ""
    },${totalActiveStakeSeconds},${Math.min(
      totalActiveStakeSeconds,
      args.activeTimestamp - args.startTimestamp
    )}`;
  });

  // eslint-disable-next-line @typescript-eslint/no-unsafe-argument, @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-call, @typescript-eslint/no-var-requires, @typescript-eslint/no-unsafe-assignment
  require("fs").writeFileSync(
    `tools/data/staked-tokens-range.csv`,
    [
      `originalMint,lastStake,totalStakeSeconds,lastStakedAt,lastUpdatedAt,totalActiveStakeSeconds,totalActiveMaxStakeSeconds`,
      ...rows,
    ].join(",\n"),
    {
      encoding: "utf-8",
    }
  ) as string;
};


