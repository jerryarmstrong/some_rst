tests/reward-distribution/update-reward-distributor.test.ts
===========================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { PublicKey } from "@solana/web3.js";
import { Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import { createRewardDistributor, createStakePool } from "../../src";
import { RewardDistributorKind } from "../../src/programs/rewardDistributor";
import { getRewardDistributor } from "../../src/programs/rewardDistributor/accounts";
import { findRewardDistributorId } from "../../src/programs/rewardDistributor/pda";
import { withUpdateRewardDistributor } from "../../src/programs/rewardDistributor/transaction";
import { createMint, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Stake and claim rewards from treasury", () => {
  const maxSupply = 100;
  let provider: CardinalProvider;
  let stakePoolId: PublicKey;
  let rewardMintId: PublicKey;

  beforeAll(async () => {
    provider = await getProvider();
    // reward mint
    [, rewardMintId] = await createMint(provider.connection, provider.wallet, {
      amount: maxSupply,
    });
  });

  it("Create Pool", async () => {
    let transaction: Transaction;
    [transaction, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {}
    );

    await executeTransaction(provider.connection, transaction, provider.wallet);
  });

  it("Create Reward Distributor", async () => {
    const [transaction] = await createRewardDistributor(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        rewardMintId: rewardMintId,
        kind: RewardDistributorKind.Treasury,
        maxSupply: new BN(maxSupply),
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const rewardDistributorData = await getRewardDistributor(
      provider.connection,
      rewardDistributorId
    );

    expect(rewardDistributorData.parsed.defaultMultiplier.toString()).toEqual(
      "1"
    );

    expect(rewardDistributorData.parsed.multiplierDecimals.toString()).toEqual(
      "0"
    );
  });

  it("Update Reward Distributor", async () => {
    const transaction = new Transaction();

    await withUpdateRewardDistributor(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        defaultMultiplier: new BN(200),
        multiplierDecimals: 2,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const rewardDistributorData = await getRewardDistributor(
      provider.connection,
      rewardDistributorId
    );

    expect(rewardDistributorData.parsed.defaultMultiplier.toString()).toEqual(
      "200"
    );

    expect(rewardDistributorData.parsed.multiplierDecimals.toString()).toEqual(
      "2"
    );
  });
});


