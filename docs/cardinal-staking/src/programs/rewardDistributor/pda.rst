src/programs/rewardDistributor/pda.ts
=====================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { utils } from "@coral-xyz/anchor";
import { PublicKey } from "@solana/web3.js";

import {
  REWARD_DISTRIBUTOR_ADDRESS,
  REWARD_DISTRIBUTOR_SEED,
  REWARD_ENTRY_SEED,
} from ".";

/**
 * Finds the reward entry id.
 * @returns
 */
export const findRewardEntryId = (
  rewardDistributorId: PublicKey,
  stakeEntryId: PublicKey
) => {
  return PublicKey.findProgramAddressSync(
    [
      utils.bytes.utf8.encode(REWARD_ENTRY_SEED),
      rewardDistributorId.toBuffer(),
      stakeEntryId.toBuffer(),
    ],
    REWARD_DISTRIBUTOR_ADDRESS
  )[0];
};

/**
 * Finds the reward distributor id.
 * @returns
 */
export const findRewardDistributorId = (stakePoolId: PublicKey) => {
  return PublicKey.findProgramAddressSync(
    [utils.bytes.utf8.encode(REWARD_DISTRIBUTOR_SEED), stakePoolId.toBuffer()],
    REWARD_DISTRIBUTOR_ADDRESS
  )[0];
};


