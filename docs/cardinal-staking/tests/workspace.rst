tests/workspace.ts
==================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { Wallet } from "@coral-xyz/anchor";
import { Connection, Keypair, LAMPORTS_PER_SOL } from "@solana/web3.js";

export type CardinalProvider = {
  connection: Connection;
  wallet: Wallet;
};

export function getConnection(): Connection {
  const url = "http://127.0.0.1:8899";
  return new Connection(url, "confirmed");
}

export async function newAccountWithLamports(
  connection: Connection,
  lamports = LAMPORTS_PER_SOL * 10,
  keypair = Keypair.generate()
): Promise<Keypair> {
  const account = keypair;
  const signature = await connection.requestAirdrop(
    account.publicKey,
    lamports
  );
  await connection.confirmTransaction(signature, "confirmed");
  return account;
}

export async function getProvider(): Promise<CardinalProvider> {
  const connection = getConnection();
  const keypair = await newAccountWithLamports(connection);
  const wallet = new Wallet(keypair);
  return {
    connection,
    wallet,
  };
}


