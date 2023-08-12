clients/cli/src/helpers/pda.ts
==============================

Last edited: 2023-08-01 17:12:05

Contents:

.. code-block:: ts

    import { PublicKey } from "@solana/web3.js";
import { PREFIX, PROGRAM_ID } from "@metaplex-foundation/mpl-token-auth-rules";

export const findRuleSetPDA = async (payer: PublicKey, name: string) => {
    return await PublicKey.findProgramAddress(
        [
            Buffer.from(PREFIX),
            payer.toBuffer(),
            Buffer.from(name),
        ],
        PROGRAM_ID,
    );
}

