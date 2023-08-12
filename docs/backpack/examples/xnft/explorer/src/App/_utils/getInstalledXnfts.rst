examples/xnft/explorer/src/App/_utils/getInstalledXnfts.ts
==========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { IdlAccounts, ProgramAccount } from "@project-serum/anchor";
import { Connection, PublicKey } from "@solana/web3.js";
import { XnftWithMetadata } from "../_types/XnftWithMetadata";
import getProgram from "./getProgram";
import { Xnft } from "./xnftIDL";

type InstallAccount = IdlAccounts<Xnft>["install"];

export default async function getInstalledXnfts(
  connection: Connection,
  pubkey: PublicKey
): Promise<string[]> {
  const program = getProgram(connection);
  const response: ProgramAccount<InstallAccount>[] =
    await program.account.install.all([
      {
        memcmp: {
          offset: 8,
          bytes: pubkey.toBase58(),
        },
      },
    ]);
  return response.map((item) => item.account.xnft.toString());
}


