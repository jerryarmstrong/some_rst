tools/stake-entries/checkStakeEntryFunds.ts
===========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import {
  decimalAmount,
  getBatchedMultipleAccounts,
  tryPublicKey,
} from "@cardinal/common";
import type { Wallet } from "@coral-xyz/anchor";
import {
  getAssociatedTokenAddressSync,
  getMint,
  unpackAccount,
} from "@solana/spl-token";
import type { Connection } from "@solana/web3.js";
import { PublicKey } from "@solana/web3.js";
import BN from "bn.js";

import { getAllStakeEntriesForPool } from "../../src/programs/stakePool/accounts";
import { chunkArray } from "../utils";

export const commandName = "checkStakeEntryFunds";
export const description = "Get all funds of a given mint in a given pool";

export const getArgs = (_connection: Connection, _wallet: Wallet) => ({
  poolIds: "BeT8h9E5BcgcMBxF7Si5GSRuB6zHcSpFuMpp6uTcVRFN",
  mintId: new PublicKey("DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"),
});

export const handler = async (
  connection: Connection,
  _wallet: Wallet,
  args: ReturnType<typeof getArgs>
) => {
  const mint = await getMint(connection, args.mintId);
  const poolIds = args.poolIds.split(",").map((pk) => tryPublicKey(pk));
  for (let pi = 0; pi < poolIds.length; pi++) {
    const poolId = poolIds[pi]!;
    const stakeEntries = await getAllStakeEntriesForPool(connection, poolId);
    console.log(`[stake-entries] (${stakeEntries.length})`);
    const stakeEntryTokenAccountIds = stakeEntries.map((entry) =>
      getAssociatedTokenAddressSync(args.mintId, entry.pubkey, true)
    );
    const chunkedIds = chunkArray(stakeEntryTokenAccountIds, 1000);
    const stakeEntryTokenAccountInfos = [];
    for (let i = 0; i < chunkedIds.length; i++) {
      const chunkIds = chunkedIds[i]!;
      console.log(
        `[loading] ${stakeEntryTokenAccountInfos.length}/${stakeEntryTokenAccountIds.length} [${chunkIds.length}]`
      );
      const chunkStakeEntryTokenAccountInfos = await getBatchedMultipleAccounts(
        connection,
        chunkIds
      );
      stakeEntryTokenAccountInfos.push(...chunkStakeEntryTokenAccountInfos);
      await new Promise((r) => setTimeout(r, 1000));
    }
    const stakeEntryTokenAccounts = stakeEntryTokenAccountInfos.map(
      (tokenAccount, i) => {
        const tokenAccountId = stakeEntryTokenAccountIds[i];
        if (tokenAccount && tokenAccountId) {
          return unpackAccount(tokenAccountId, tokenAccount);
        }
        return null;
      }
    );

    const totalTokens = stakeEntryTokenAccounts.reduce(
      (acc, tokenAccount) =>
        tokenAccount ? new BN(tokenAccount?.amount.toString()).add(acc) : acc,
      new BN(0)
    );

    const pools = {} as { [pid: string]: BN };
    for (let i = 0; i < stakeEntries.length; i++) {
      const stakeEntry = stakeEntries[i];
      const stakeEntryTokenAccount = stakeEntryTokenAccounts[i];
      if (stakeEntry && stakeEntryTokenAccount) {
        const current = pools[stakeEntry.parsed.pool.toString()];
        pools[stakeEntry.parsed.pool.toString()] = (current ?? new BN(0)).add(
          new BN(stakeEntryTokenAccount.amount.toString())
        );
      }
    }
    console.log(`[total] ${decimalAmount(totalTokens, mint.decimals)}`);
    console.log(`[breakdown] ${JSON.stringify(pools, null, 2)}`);
  }
};


