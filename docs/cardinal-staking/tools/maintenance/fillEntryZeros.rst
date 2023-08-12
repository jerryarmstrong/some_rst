tools/maintenance/fillEntryZeros.ts
===================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { AccountData } from "@cardinal/common";
import {
  AnchorProvider,
  BorshAccountsCoder,
  Program,
  utils,
  Wallet,
} from "@coral-xyz/anchor";
import type { Connection } from "@solana/web3.js";
import { Keypair, Transaction } from "@solana/web3.js";
import * as dotenv from "dotenv";

import { executeTransaction } from "../../src";
import type {
  STAKE_POOL_PROGRAM,
  StakeEntryData,
} from "../../src/programs/stakePool";
import {
  STAKE_POOL_ADDRESS,
  STAKE_POOL_IDL,
} from "../../src/programs/stakePool";
import { connectionFor } from "../connection";
import { chunkArray } from "../utils";

dotenv.config();

const wallet = Keypair.fromSecretKey(
  utils.bytes.bs58.decode(process.env.WALLET || "")
);
const CLUSTER = "devnet";
const BATCH_SIZE = 20;
const PARALLEL_TRANSACTIONS = 100;
const MAX_RETRIES = 3;
const DRY_RUN = false;
const ALLOWED_ENTRY_IDS: string[] = [];

export const getAllStakeEntries = async (connection: Connection) => {
  const programAccounts = await connection.getProgramAccounts(
    STAKE_POOL_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("stakeEntry")
            ),
          },
        },
      ],
    }
  );
  return programAccounts;
};

const fillEntryZeros = async (cluster: string) => {
  console.log(`wallet=${wallet.publicKey.toString()}`);
  // setup
  const connection = connectionFor(cluster);
  const provider = new AnchorProvider(connection, new Wallet(wallet), {});
  const stakePoolProgram = new Program<STAKE_POOL_PROGRAM>(
    STAKE_POOL_IDL,
    STAKE_POOL_ADDRESS,
    provider
  );

  const allStakeEntries = await getAllStakeEntries(connection);

  //// parsed
  const parsedStakeEntries: AccountData<StakeEntryData>[] = [];
  const poolCounts: { [poolId: string]: number } = {};
  for (let i = 0; i < allStakeEntries.length; i++) {
    const a = allStakeEntries[i]!;
    try {
      const stakeEntryData: StakeEntryData =
        stakePoolProgram.coder.accounts.decode("stakeEntry", a.account.data);
      const encoded = await stakePoolProgram.coder.accounts.encode(
        "stakeEntry",
        stakeEntryData
      );
      if (a.account.data.slice(encoded.length).some((b) => b !== 0)) {
        const poolId = stakeEntryData.pool.toString();
        const c = poolCounts[poolId] ?? 0;
        poolCounts[poolId] = c + 1;
        parsedStakeEntries.push({ pubkey: a.pubkey, parsed: stakeEntryData });
      }
    } catch (e) {
      // console.log(`[error] ${a.pubkey.toString()}`, e);
    }
  }

  console.log(poolCounts);

  const filteredEntries = parsedStakeEntries.filter((p) =>
    ALLOWED_ENTRY_IDS.length > 0
      ? ALLOWED_ENTRY_IDS.includes(p.pubkey.toString())
      : true
  );
  const transactionsData: {
    transaction: Transaction;
    accountsInTx: AccountData<StakeEntryData>[];
  }[] = [];

  console.log(`\nTotal=${filteredEntries.length}`);
  const chunkedEntries = chunkArray(filteredEntries, BATCH_SIZE);
  for (let i = 0; i < chunkedEntries.length; i++) {
    const stakeEntries = chunkedEntries[i]!;
    console.log(`\n>> (${i + 1}/${chunkedEntries.length})`);
    const transaction = new Transaction();
    const accountsInTx: AccountData<StakeEntryData>[] = [];
    for (let j = 0; j < stakeEntries.length; j++) {
      const stakeEntryData = stakeEntries[j]!;
      console.log(`>>> Entry (${stakeEntryData.pubkey.toString()})`);
      console.log(stakeEntryData);
      try {
        transaction.add(
          stakePoolProgram.instruction.stakeEntryFillZeros({
            accounts: {
              stakeEntry: stakeEntryData.pubkey,
            },
          })
        );
        accountsInTx.push(stakeEntryData);
      } catch (e: unknown) {
        console.log(
          `Failed to add IXs for pool (${stakeEntryData.pubkey.toString()})`
        );
      }
    }

    transactionsData.push({
      transaction,
      accountsInTx,
    });
  }

  console.log(`\n\nTransactions=${transactionsData.length}`);

  const chunkedTxDatas = chunkArray(transactionsData, PARALLEL_TRANSACTIONS);
  for (let i = 0; i < chunkedTxDatas.length; i++) {
    const txDatas = chunkedTxDatas[i]!;
    console.log(`> (${i + 1}/${chunkedTxDatas.length})`);
    await Promise.all(
      txDatas.map(async ({ transaction, accountsInTx }) => {
        let attempts = 0;
        let txid;
        while (attempts <= MAX_RETRIES && !txid) {
          try {
            if (!DRY_RUN && transaction.instructions.length > 0) {
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
  }
};

fillEntryZeros(CLUSTER).catch((e) => console.log(e));


