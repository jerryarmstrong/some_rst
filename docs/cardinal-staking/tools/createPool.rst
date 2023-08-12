tools/createPool.ts
===================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { executeTransaction } from "@cardinal/common";
import { utils, Wallet } from "@coral-xyz/anchor";
import { Keypair, Transaction } from "@solana/web3.js";

import { withInitStakePool } from "../src/programs/stakePool/transaction";
import { connectionFor } from "./connection";

const wallet = new Wallet(Keypair.fromSecretKey(utils.bytes.bs58.decode("")));

const main = async () => {
  const connection = connectionFor("mainnet");
  const transaction = new Transaction();
  await withInitStakePool(transaction, connection, wallet, {});
  const txid = await executeTransaction(connection, transaction, wallet);
  console.log(txid);
};

main().catch((e) => console.log(e));


