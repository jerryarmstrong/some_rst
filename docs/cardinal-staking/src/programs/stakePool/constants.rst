src/programs/stakePool/constants.ts
===================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { ParsedIdlAccountData } from "@cardinal/common";
import { emptyWallet } from "@cardinal/common";
import { AnchorProvider, Program } from "@coral-xyz/anchor";
import type { Wallet } from "@coral-xyz/anchor/dist/cjs/provider";
import type { ConfirmOptions, Connection } from "@solana/web3.js";
import { Keypair, PublicKey } from "@solana/web3.js";

import * as STAKE_POOL_TYPES from "../../idl/cardinal_stake_pool";

export const STAKE_POOL_ADDRESS = new PublicKey(
  "stkBL96RZkjY5ine4TvPihGqW8UHJfch2cokjAPzV8i"
);

export const STAKE_POOL_SEED = "stake-pool";

export const STAKE_ENTRY_SEED = "stake-entry";

export const GROUP_ENTRY_SEED = "group-entry";

export const IDENTIFIER_SEED = "identifier";

export const STAKE_AUTHORIZATION_SEED = "stake-authorization";

export const STAKE_BOOSTER_SEED = "stake-booster";

export const AUTHORITY_OFFSET = 25;
export const STAKER_OFFSET = 82;
export const GROUP_STAKER_OFFSET = 8 + 1 + 32;
export const POOL_OFFSET = 9;

export type STAKE_POOL_PROGRAM = STAKE_POOL_TYPES.CardinalStakePool;

export const STAKE_POOL_IDL = STAKE_POOL_TYPES.IDL;

export type StakePoolData = ParsedIdlAccountData<
  "stakePool",
  STAKE_POOL_PROGRAM
>;
export type StakeEntryData = ParsedIdlAccountData<
  "stakeEntry",
  STAKE_POOL_PROGRAM
>;
export type GroupStakeEntryData = ParsedIdlAccountData<
  "groupStakeEntry",
  STAKE_POOL_PROGRAM
>;
export type IdentifierData = ParsedIdlAccountData<
  "identifier",
  STAKE_POOL_PROGRAM
>;
export type StakeAuthorizationData = ParsedIdlAccountData<
  "stakeAuthorizationRecord",
  STAKE_POOL_PROGRAM
>;
export type StakeBoosterData = ParsedIdlAccountData<
  "stakeBooster",
  STAKE_POOL_PROGRAM
>;

export const STAKE_BOOSTER_PAYMENT_MANAGER_NAME = "cardinal-stake-booster";
export const STAKE_BOOSTER_PAYMENT_MANAGER = new PublicKey(
  "CuEDMUqgkGTVcAaqEDHuVR848XN38MPsD11JrkxcGD6a" // cardinal-stake-booster
);

export enum ReceiptType {
  // Receive the original mint wrapped in a token manager
  Original = 1,
  // Receive a receipt mint wrapped in a token manager
  Receipt = 2,
  // Receive nothing
  None = 3,
}

export const stakePoolProgram = (
  connection: Connection,
  wallet?: Wallet,
  confirmOptions?: ConfirmOptions
) => {
  return new Program<STAKE_POOL_PROGRAM>(
    STAKE_POOL_IDL,
    STAKE_POOL_ADDRESS,
    new AnchorProvider(
      connection,
      wallet ?? emptyWallet(Keypair.generate().publicKey),
      confirmOptions ?? {}
    )
  );
};


