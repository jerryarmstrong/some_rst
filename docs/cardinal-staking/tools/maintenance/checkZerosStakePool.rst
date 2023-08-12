tools/maintenance/checkZerosStakePool.ts
========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { BorshAccountsCoder, utils } from "@coral-xyz/anchor";
import type { Connection } from "@solana/web3.js";

import type { RewardDistributorData } from "../../src/programs/rewardDistributor";
import {
  REWARD_DISTRIBUTOR_ADDRESS,
  REWARD_DISTRIBUTOR_IDL,
} from "../../src/programs/rewardDistributor";
import { connectionFor } from "../connection";

const CLUSTER = "mainnet";
// const MAX_SIZE = 400;

export const getAllRewardDistributors = async (connection: Connection) => {
  const programAccounts = await connection.getProgramAccounts(
    REWARD_DISTRIBUTOR_ADDRESS,
    {
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: utils.bytes.bs58.encode(
              BorshAccountsCoder.accountDiscriminator("rewardDistributor")
            ),
          },
        },
      ],
    }
  );
  return programAccounts;
};

const checkZeros = async (cluster: string) => {
  const connection = connectionFor(cluster);
  const coder = new BorshAccountsCoder(REWARD_DISTRIBUTOR_IDL);
  const allRewardDistributors = await getAllRewardDistributors(connection);
  console.log(
    `--------- Check zeros ${allRewardDistributors.length} reward distributors ---------`
  );
  for (let i = 0; i < allRewardDistributors.length; i++) {
    const r = allRewardDistributors[i]!;
    const rewardDistributorData: RewardDistributorData = coder.decode(
      "rewardDistributor",
      r.account.data
    );
    const encoded = await coder.encode(
      "rewardDistributor",
      rewardDistributorData
    );
    if (r.account.data.slice(encoded.length).some((b) => b !== 0)) {
      console.log(r.pubkey.toString(), rewardDistributorData);
    }
  }
};

checkZeros(CLUSTER).catch((e) => console.log(e));


