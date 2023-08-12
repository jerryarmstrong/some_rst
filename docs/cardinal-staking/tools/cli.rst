tools/cli.ts
============

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { Wallet } from "@coral-xyz/anchor";
import type { Cluster, Connection } from "@solana/web3.js";
import * as dotenv from "dotenv";
import * as readline from "readline";
import type { ArgumentsCamelCase, CommandModule } from "yargs";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";

import * as claimRewardsForUsers from "./admin-actions/claimRewardsForUsers";
import * as initializeEntriesAndSetMultipliers from "./admin-actions/initializeEntriesAndSetMultipliers";
import * as updateMultipliersOnRules from "./admin-actions/updateMultipliersOnRules";
import * as getAllStakePools from "./analytics/getAllStakePools";
import * as stakedTokensBreakdownByWallet from "./analytics/stakedTokensBreakdownByWallet";
import * as stakedTokensTimeRange from "./analytics/stakedTokensTimeRange";
import { connectionFor } from "./connection";
import * as reclaimFunds from "./reward-distributor/reclaimFunds";
import * as transferTokens from "./reward-distributor/transferTokens";
import * as checkStakeEntryFunds from "./stake-entries/checkStakeEntryFunds";
import { keypairFrom } from "./utils";

dotenv.config();

export type ProviderParams = {
  cluster: string;
  wallet: string;
};

const commandBuilder = <T>(command: {
  commandName: string;
  description: string;
  getArgs: (c: Connection, w: Wallet) => T;
  handler: (c: Connection, w: Wallet, a: T) => Promise<void>;
}): CommandModule<ProviderParams, ProviderParams> => {
  return {
    command: command.commandName,
    describe: command.description,
    handler: async ({
      cluster,
      wallet,
    }: ArgumentsCamelCase<ProviderParams>) => {
      const clusterString = process.env.CLUSTER || cluster;
      const c = connectionFor(clusterString as Cluster);
      const w = new Wallet(keypairFrom(process.env.WALLET || wallet, "wallet"));
      const a = command.getArgs(c, w);
      console.log(command.description);
      console.log(
        `[cluster=${clusterString}] [wallet=${w.publicKey.toString()}]`
      );
      console.log(`\n(modify args in ${command.commandName}.ts)`);
      console.log(JSON.stringify(a, null, 2));
      await question("\nExecute... [enter]");
      await command.handler(c, w, a);
    },
  };
};

export const question = async (query: string) => {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  return new Promise((resolve) =>
    rl.question(query, (ans) => {
      rl.close();
      resolve(ans);
    })
  );
};

void yargs(hideBin(process.argv))
  .positional("wallet", {
    describe: "Wallet to use - default to WALLET environment variable",
    default: "~/.config/solana/id.json",
  })
  .positional("cluster", {
    describe:
      "Solana cluster moniker to use [mainnet, devnet] - ovverride url with RPC_URL environment variable or mainnet moniker with MAINNET_PRIMARY environment variable",
    default: "devnet",
  })
  // analytics
  .command(commandBuilder(stakedTokensBreakdownByWallet))
  .command(commandBuilder(stakedTokensTimeRange))
  .command(commandBuilder(getAllStakePools))
  // admin-actions
  .command(commandBuilder(updateMultipliersOnRules))
  .command(commandBuilder(initializeEntriesAndSetMultipliers))
  .command(commandBuilder(claimRewardsForUsers))
  // reward-distributor
  .command(commandBuilder(reclaimFunds))
  .command(commandBuilder(transferTokens))
  // stake-entries
  .command(commandBuilder(checkStakeEntryFunds))
  .strict()
  .demandCommand()
  .alias({ h: "help" }).argv;


