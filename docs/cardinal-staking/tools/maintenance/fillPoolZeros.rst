tools/maintenance/fillPoolZeros.ts
==================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { AccountData } from "@cardinal/common";
import { AnchorProvider, Program, utils, Wallet } from "@coral-xyz/anchor";
import { Keypair, Transaction } from "@solana/web3.js";

import { executeTransaction } from "../../src";
import type {
  STAKE_POOL_PROGRAM,
  StakePoolData,
} from "../../src/programs/stakePool";
import {
  STAKE_POOL_ADDRESS,
  STAKE_POOL_IDL,
} from "../../src/programs/stakePool";
import { getAllStakePools } from "../../src/programs/stakePool/accounts";
import { connectionFor } from "../connection";
import { chunkArray } from "../utils";

const wallet = Keypair.fromSecretKey(utils.bytes.bs58.decode(""));

const CLUSTER = "devnet";
const BATCH_SIZE = 20;
const MAX_RETRIES = 3;
const MAX_SIZE = 400;
const DRY_RUN = false;
const ALLOWED_POOL_IDS = ["2s3qXuGyMNedXS61Vi9XsRx7HuryyyZUYGyMtCrKUXva"];

const fillPoolZeros = async (cluster: string) => {
  console.log(wallet.publicKey.toString());
  const connection = connectionFor(cluster);
  const provider = new AnchorProvider(connection, new Wallet(wallet), {});
  const stakePoolProgram = new Program<STAKE_POOL_PROGRAM>(
    STAKE_POOL_IDL,
    STAKE_POOL_ADDRESS,
    provider
  );

  const allStakePools = (await getAllStakePools(connection))
    .filter((p) => ALLOWED_POOL_IDS.includes(p.pubkey.toString()))
    .slice(0, MAX_SIZE);
  console.log(`--------- Fill zeros ${allStakePools.length} pools ---------`);

  const transactionsData: {
    transaction: Transaction;
    accountsInTx: AccountData<StakePoolData>[];
  }[] = [];
  const chunkedPools = chunkArray(allStakePools, BATCH_SIZE);
  for (let i = 0; i < chunkedPools.length; i++) {
    const stakePools = chunkedPools[i]!;
    console.log(
      `\n\n-------- Chunk ${i + 1} of ${chunkedPools.length} --------`
    );
    const transaction = new Transaction();
    const accountsInTx: AccountData<StakePoolData>[] = [];
    for (let j = 0; j < stakePools.length; j++) {
      const stakePoolData = stakePools[j]!;
      console.log(`>> Pool (${stakePoolData.pubkey.toString()})`);
      try {
        transaction.add(
          stakePoolProgram.instruction.stakePoolFillZeros({
            accounts: {
              stakePool: stakePoolData.pubkey,
            },
          })
        );
        accountsInTx.push(stakePoolData);
      } catch (e: unknown) {
        console.log(
          `Failed to add IXs for pool (${stakePoolData.pubkey.toString()})`
        );
      }
    }

    transactionsData.push({
      transaction,
      accountsInTx,
    });
  }

  console.log(`\n\n--------- Results ---------`);
  await Promise.all(
    transactionsData.map(async ({ transaction, accountsInTx }) => {
      let attempts = 0;
      let txid;
      while (attempts <= MAX_RETRIES && !txid) {
        try {
          if (!DRY_RUN) {
            txid = await executeTransaction(
              connection,
              new Wallet(wallet),
              transaction,
              {}
            );
          }
        } catch (e) {
          console.log(e);
        }
        attempts += 1;
      }
      if (txid) {
        console.log(
          `Succesful [${accountsInTx
            .map((e) => e.pubkey.toString())
            .join()}] with transaction ${txid} (https://explorer.solana.com/tx/${txid}?cluster=${cluster})`
        );
      } else {
        console.log(
          `Failed [${accountsInTx.map((e) => e.pubkey.toString()).join()}]`
        );
      }
    })
  );
};

fillPoolZeros(CLUSTER).catch((e) => console.log(e));


