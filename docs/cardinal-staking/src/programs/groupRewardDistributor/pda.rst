src/programs/groupRewardDistributor/pda.ts
==========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { utils } from "@coral-xyz/anchor";
import { PublicKey } from "@solana/web3.js";

import {
  GROUP_REWARD_COUNTER_SEED,
  GROUP_REWARD_DISTRIBUTOR_ADDRESS,
  GROUP_REWARD_DISTRIBUTOR_SEED,
  GROUP_REWARD_ENTRY_SEED,
} from "./constants";

/**
 * Finds the group reward entry id.
 * @returns
 */
export const findGroupRewardEntryId = (
  groupRewardDistributorId: PublicKey,
  groupEntryId: PublicKey
) => {
  return PublicKey.findProgramAddressSync(
    [
      utils.bytes.utf8.encode(GROUP_REWARD_ENTRY_SEED),
      groupRewardDistributorId.toBuffer(),
      groupEntryId.toBuffer(),
    ],
    GROUP_REWARD_DISTRIBUTOR_ADDRESS
  )[0];
};

/**
 * Finds the group reward entry id.
 * @returns
 */
export const findGroupRewardCounterId = (
  groupRewardDistributorId: PublicKey,
  authority: PublicKey
) => {
  return PublicKey.findProgramAddressSync(
    [
      utils.bytes.utf8.encode(GROUP_REWARD_COUNTER_SEED),
      groupRewardDistributorId.toBuffer(),
      authority.toBuffer(),
    ],
    GROUP_REWARD_DISTRIBUTOR_ADDRESS
  )[0];
};

/**
 * Finds the group reward distributor id.
 * @returns
 */
export const findGroupRewardDistributorId = (id: PublicKey) => {
  return PublicKey.findProgramAddressSync(
    [utils.bytes.utf8.encode(GROUP_REWARD_DISTRIBUTOR_SEED), id.toBuffer()],
    GROUP_REWARD_DISTRIBUTOR_ADDRESS
  )[0];
};


