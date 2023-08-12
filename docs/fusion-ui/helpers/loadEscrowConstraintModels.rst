helpers/loadEscrowConstraintModels.ts
=====================================

Last edited: 2023-02-28 18:04:35

Contents:

.. code-block:: ts

    import { Connection, PublicKey } from "@solana/web3.js";
import {
  EscrowConstraintModel,
  PROGRAM_ADDRESS,
} from "@metaplex-foundation/mpl-trifle/dist/src/generated";

export const loadEscrowConstraintModels = async (
  publicKey: PublicKey,
  connection: Connection,
): Promise<Record<string, EscrowConstraintModel>> => {
  const accountInfos = await connection.getProgramAccounts(
    new PublicKey(PROGRAM_ADDRESS),
    {
      filters: [{ memcmp: { offset: 1, bytes: publicKey.toBase58() } }],
    },
  );

  console.log("accountInfos", accountInfos);
  return accountInfos.reduce((acc, accountInfo) => {
    return {
      ...acc,
      [accountInfo.pubkey.toBase58()]:
        EscrowConstraintModel.fromAccountInfo(accountInfo.account, 0)[0],
    };
  }, {});
};


