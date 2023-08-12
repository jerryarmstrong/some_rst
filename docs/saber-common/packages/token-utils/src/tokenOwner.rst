packages/token-utils/src/tokenOwner.ts
======================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    import type { PublicKey } from "@saberhq/solana-contrib";
import type { TransactionInstruction } from "@solana/web3.js";
import { createAssociatedTokenAccountInstruction,
  createMintToInstruction,
  createTransferCheckedInstruction,
  createTransferInstruction} from "@solana/spl-token";
import {
  ASSOCIATED_TOKEN_PROGRAM_ID,
  getATAAddress,
  getATAAddressSync,
  TOKEN_PROGRAM_ID,
} from "./index.js";
import type { TokenAmount } from "./tokenAmount.js";

/**
 * Wrapper around a token account owner to create token instructions.
 */
export class TokenOwner {
  constructor(readonly owner: PublicKey) {}

  /**
   * Gets the user's ATA.
   * @param mint
   * @returns
   */
  async getATA(mint: PublicKey): Promise<PublicKey> {
    return await getATAAddress({ mint, owner: this.owner });
  }

  /**
   * Gets the user's ATA.
   * @param mint
   * @returns
   */
  getATASync(mint: PublicKey): PublicKey {
    return getATAAddressSync({ mint, owner: this.owner });
  }

  /**
   * Transfers tokens to a token account.
   * @param amount Amount of tokens to transfer.
   * @param to Token account to transfer to.
   * @returns The transaction instruction.
   */
  async transfer(
    amount: TokenAmount,
    to: PublicKey
  ): Promise<TransactionInstruction> {
    // return SPLToken.createTransferInstruction(
    //   TOKEN_PROGRAM_ID,
    //   await this.getATA(amount.token.mintAccount),
    //   to,
    //   this.owner,
    //   [],
    //   amount.toU64()
    // );
    return createTransferInstruction(
      await this.getATA(amount.token.mintAccount),
      to,
      this.owner,
      amount.toU64(),
      [],
      TOKEN_PROGRAM_ID,
    );
  }

  /**
   * Transfers tokens to a token account, checked..
   * @param amount Amount of tokens to transfer.
   * @param to Token account to transfer to.
   * @returns The transaction instruction.
   */
  async transferChecked(
    amount: TokenAmount,
    to: PublicKey
  ): Promise<TransactionInstruction> {
    // return SPLToken.createTransferCheckedInstruction(
    //   TOKEN_PROGRAM_ID,
    //   await this.getATA(amount.token.mintAccount),
    //   amount.token.mintAccount,
    //   to,
    //   this.owner,
    //   [],
    //   amount.toU64(),
    //   amount.token.decimals
    // );
    return createTransferCheckedInstruction(
      await this.getATA(amount.token.mintAccount),
      amount.token.mintAccount,
      to,
      this.owner,
      amount.toU64(),
      amount.token.decimals,
      [],
      TOKEN_PROGRAM_ID
    );
  }

  /**
   * Mints tokens to a token account.
   * @param amount Amount of tokens to transfer.
   * @param to Token account to transfer to.
   * @returns The transaction instruction.
   */
  mintTo(amount: TokenAmount, to: PublicKey): TransactionInstruction {
    // return SPLToken.createMintToInstruction(
    //   TOKEN_PROGRAM_ID,
    //   amount.token.mintAccount,
    //   to,
    //   this.owner,
    //   [],
    //   amount.toU64()
    // );
    return createMintToInstruction(
      amount.token.mintAccount,
      to,
      this.owner,
      amount.toU64(),
      [],
      TOKEN_PROGRAM_ID,
    );
  }

  /**
   * Creates an associated token account instruction.
   * @param mint Mint of the ATA.
   * @param payer Payer to create the ATA. Defaults to the owner.
   * @returns The transaction instruction.
   */
  async createATA(
    mint: PublicKey,
    payer: PublicKey = this.owner
  ): Promise<TransactionInstruction> {
    return createAssociatedTokenAccountInstruction(
      payer,
      await this.getATA(mint),
      this.owner,
      mint,
      TOKEN_PROGRAM_ID,
      ASSOCIATED_TOKEN_PROGRAM_ID,
    );
    // return SPLToken.createAssociatedTokenAccountInstruction(
    //   ASSOCIATED_TOKEN_PROGRAM_ID,
    //   TOKEN_PROGRAM_ID,
    //   mint,
    //   await this.getATA(mint),
    //   this.owner,
    //   payer
    // );
  }
}


