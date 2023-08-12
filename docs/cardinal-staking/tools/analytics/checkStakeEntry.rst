tools/analytics/checkStakeEntry.ts
==================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { Keypair, PublicKey } from "@solana/web3.js";

import { getRewardEntry } from "../../src/programs/rewardDistributor/accounts";
import {
  findRewardDistributorId,
  findRewardEntryId,
} from "../../src/programs/rewardDistributor/pda";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { connectionFor } from "../connection";

const checkStakeEntry = async (
  cluster: string,
  stakePoolId: PublicKey,
  mintId: PublicKey
) => {
  const connection = connectionFor(cluster);
  const stakeEntryId = await findStakeEntryIdFromMint(
    connection,
    Keypair.generate().publicKey,
    stakePoolId,
    mintId,
    false
  );

  const stakeEntry = await getStakeEntry(connection, stakeEntryId);
  console.log(stakeEntry);
  const rewardDistributorId = findRewardDistributorId(stakePoolId);

  const rewardEntryId = findRewardEntryId(rewardDistributorId, stakeEntryId);

  const rewardEntry = await getRewardEntry(connection, rewardEntryId);
  console.log(rewardEntry);
};

checkStakeEntry(
  "mainnet",
  new PublicKey("3BZCupFU6X3wYJwgTsKS2vTs4VeMrhSZgx4P2TfzExtP"),
  new PublicKey("2eRCM7sSKuYKiSpEssZTxzKTfPiMbs4JFBwbeeDS3w71")
).catch((e) => console.log(e));


