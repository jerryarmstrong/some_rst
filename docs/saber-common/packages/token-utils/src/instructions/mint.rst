packages/token-utils/src/instructions/mint.ts
=============================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    import type { Provider } from "@saberhq/solana-contrib";
import { TransactionEnvelope } from "@saberhq/solana-contrib";
// import type { u64 } from "@solana/buffer-layout-utils";
import {
  createInitializeMintInstruction,
  createMintToInstruction as _createMintToInstruction,
  getMinimumBalanceForRentExemptMint,
  TOKEN_PROGRAM_ID,
} from "@solana/spl-token";
import type { PublicKey, Signer } from "@solana/web3.js";
import { SystemProgram } from "@solana/web3.js";

import { MintLayout } from "../layout.js";

/**
 * Creates instructions for initializing a mint.
 * @param param0
 * @returns
 */
export const createInitMintInstructions = async ({
  provider,
  mintKP,
  decimals,
  mintAuthority = provider.wallet.publicKey,
  freezeAuthority = null,
}: {
  provider: Provider;
  mintKP: Signer;
  decimals: number;
  mintAuthority?: PublicKey;
  freezeAuthority?: PublicKey | null;
}): Promise<TransactionEnvelope> => {
  return createInitMintTX({
    provider,
    mintKP,
    decimals,
    // rentExemptMintBalance:await SPLToken.getMinBalanceRentForExemptMint(
    rentExemptMintBalance: await getMinimumBalanceForRentExemptMint(
      provider.connection
    ),
    mintAuthority,
    freezeAuthority,
  });
};

/**
 * Creates instructions for initializing a mint.
 * @param param0
 * @returns
 */
export const createInitMintTX = ({
  provider,
  mintKP,
  decimals,
  rentExemptMintBalance,
  mintAuthority = provider.wallet.publicKey,
  freezeAuthority = null,
}: {
  provider: Provider;
  mintKP: Signer;
  decimals: number;
  rentExemptMintBalance: number;
  mintAuthority?: PublicKey;
  freezeAuthority?: PublicKey | null;
}): TransactionEnvelope => {
  const from = provider.wallet.publicKey;
  return new TransactionEnvelope(
    provider,
    [
      SystemProgram.createAccount({
        fromPubkey: from,
        newAccountPubkey: mintKP.publicKey,
        space: MintLayout.span,
        lamports: rentExemptMintBalance,
        programId: TOKEN_PROGRAM_ID,
      }),
      // SPLToken.createInitMintInstruction(
      //   TOKEN_PROGRAM_ID,
      //   mintKP.publicKey,
      //   decimals,
      //   mintAuthority,
      //   freezeAuthority
      // ),
      createInitializeMintInstruction(
        mintKP.publicKey,
        decimals,
        mintAuthority,
        freezeAuthority,
        TOKEN_PROGRAM_ID
      ),
    ],
    [mintKP]
  );
};

export const createMintToInstruction = ({
  provider,
  mint,
  mintAuthorityKP,
  to,
  amount,
}: {
  provider: Provider;
  mint: PublicKey;
  mintAuthorityKP: Signer;
  to: PublicKey;
  amount: bigint;
}): TransactionEnvelope => {
  return new TransactionEnvelope(
    provider,
    [
      // SPLToken.createMintToInstruction(
      //   TOKEN_PROGRAM_ID,
      //   mint,
      //   to,
      //   mintAuthorityKP.publicKey,
      //   [],
      //   amount
      // ),
      _createMintToInstruction(
        mint,
        to,
        mintAuthorityKP.publicKey,
        amount,
        [],
        TOKEN_PROGRAM_ID
      ),
    ],
    [mintAuthorityKP]
  );
};


