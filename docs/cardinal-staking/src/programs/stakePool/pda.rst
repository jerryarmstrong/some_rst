src/programs/stakePool/pda.ts
=============================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { BN, utils } from "@coral-xyz/anchor";
import { PublicKey } from "@solana/web3.js";

import { STAKE_ENTRY_SEED, STAKE_POOL_ADDRESS, STAKE_POOL_SEED } from ".";
import {
  GROUP_ENTRY_SEED,
  IDENTIFIER_SEED,
  STAKE_AUTHORIZATION_SEED,
  STAKE_BOOSTER_SEED,
} from "./constants";

/**
 * Finds the stake pool id.
 * @returns
 */
export const findStakePoolId = (identifier: BN): PublicKey => {
  return PublicKey.findProgramAddressSync(
    [
      utils.bytes.utf8.encode(STAKE_POOL_SEED),
      identifier.toArrayLike(Buffer, "le", 8),
    ],
    STAKE_POOL_ADDRESS
  )[0];
};

/**
 * Convenience method to find the stake entry id.
 * @returns
 */
export const findStakeEntryId = (
  wallet: PublicKey,
  stakePoolId: PublicKey,
  originalMintId: PublicKey,
  isFungible: boolean
): PublicKey => {
  return PublicKey.findProgramAddressSync(
    [
      utils.bytes.utf8.encode(STAKE_ENTRY_SEED),
      stakePoolId.toBuffer(),
      originalMintId.toBuffer(),
      isFungible ? wallet.toBuffer() : PublicKey.default.toBuffer(),
    ],
    STAKE_POOL_ADDRESS
  )[0];
};

/**
 * Finds the identifier id.
 * @returns
 */
export const findIdentifierId = (): PublicKey => {
  return PublicKey.findProgramAddressSync(
    [utils.bytes.utf8.encode(IDENTIFIER_SEED)],
    STAKE_POOL_ADDRESS
  )[0];
};

/**
 * Find stake authorization id.
 * @returns
 */
export const findStakeAuthorizationId = (
  stakePoolId: PublicKey,
  mintId: PublicKey
): PublicKey => {
  return PublicKey.findProgramAddressSync(
    [
      utils.bytes.utf8.encode(STAKE_AUTHORIZATION_SEED),
      stakePoolId.toBuffer(),
      mintId.toBuffer(),
    ],
    STAKE_POOL_ADDRESS
  )[0];
};

/**
 * Find stake booster id.
 * @returns
 */
export const findStakeBoosterId = (
  stakePoolId: PublicKey,
  identifier?: BN
): PublicKey => {
  return PublicKey.findProgramAddressSync(
    [
      utils.bytes.utf8.encode(STAKE_BOOSTER_SEED),
      stakePoolId.toBuffer(),
      (identifier ?? new BN(0)).toArrayLike(Buffer, "le", 8),
    ],
    STAKE_POOL_ADDRESS
  )[0];
};

/**
 * Convenience method to find the stake entry id.
 * @returns
 */
export const findGroupEntryId = (id: PublicKey): PublicKey => {
  return PublicKey.findProgramAddressSync(
    [utils.bytes.utf8.encode(GROUP_ENTRY_SEED), id.toBuffer()],
    STAKE_POOL_ADDRESS
  )[0];
};


