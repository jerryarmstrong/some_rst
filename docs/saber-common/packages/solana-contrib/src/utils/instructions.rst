packages/solana-contrib/src/utils/instructions.ts
=================================================

Last edited: 2023-06-29 16:13:38

Contents:

.. code-block:: ts

    import { PublicKey, TransactionInstruction } from "@solana/web3.js";

/**
 * ID of the memo program.
 */
export const MEMO_PROGRAM_ID = new PublicKey(
  "MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr"
);

/**
 * Creates a memo program instruction.
 *
 * More info: https://spl.solana.com/memo
 *
 * @param text Text of the memo.
 * @param signers Optional signers to validate.
 * @returns
 */
export const createMemoInstruction = (
  text: string,
  signers: readonly PublicKey[] = []
): TransactionInstruction => {
  return new TransactionInstruction({
    programId: MEMO_PROGRAM_ID,
    keys: signers.map((s) => ({
      pubkey: s,
      isSigner: true,
      isWritable: false,
    })),
    data: Buffer.from(text, "utf8"),
  });
};


