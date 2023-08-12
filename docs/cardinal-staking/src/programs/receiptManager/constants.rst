src/programs/receiptManager/constants.ts
========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { ParsedIdlAccountData } from "@cardinal/common";
import { emptyWallet } from "@cardinal/common";
import { AnchorProvider, Program } from "@coral-xyz/anchor";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import type { ConfirmOptions, Connection } from "@solana/web3.js";
import { Keypair, PublicKey } from "@solana/web3.js";

import * as RECEIPT_MANAGER_TYPES from "../../idl/cardinal_receipt_manager";

export const RECEIPT_MANAGER_ADDRESS = new PublicKey(
  "rrmevmpXMooxn8Qu6u7RWao93BZn4cKgfjtNMURSc2E"
);

export const RECEIPT_MANAGER_SEED = "receipt-manager";
export const REWARD_RECEIPT_SEED = "reward-receipt";
export const RECEIPT_ENTRY_SEED = "receipt-entry";

export type RECEIPT_MANAGER_PROGRAM =
  RECEIPT_MANAGER_TYPES.CardinalReceiptManager;

export const RECEIPT_MANAGER_IDL = RECEIPT_MANAGER_TYPES.IDL;

export type ReceiptManagerData = ParsedIdlAccountData<
  "receiptManager",
  RECEIPT_MANAGER_PROGRAM
>;
export type RewardReceiptData = ParsedIdlAccountData<
  "rewardReceipt",
  RECEIPT_MANAGER_PROGRAM
>;
export type ReceiptEntryData = ParsedIdlAccountData<
  "receiptEntry",
  RECEIPT_MANAGER_PROGRAM
>;

export const RECEIPT_MANAGER_PAYMENT_MANAGER_NAME = "cardinal-receipt-manager";
export const RECEIPT_MANAGER_PAYMENT_MANAGER = new PublicKey(
  "FQJ2czigCYygS8v8trLU7TBAi7NjRN1h1C2vLAh2GYDi" // cardinal-receipt-manager
);

export const receiptManagerProgram = (
  connection: Connection,
  wallet?: Wallet,
  confirmOptions?: ConfirmOptions
) => {
  return new Program<RECEIPT_MANAGER_PROGRAM>(
    RECEIPT_MANAGER_IDL,
    RECEIPT_MANAGER_ADDRESS,
    new AnchorProvider(
      connection,
      wallet ?? emptyWallet(Keypair.generate().publicKey),
      confirmOptions ?? {}
    )
  );
};


