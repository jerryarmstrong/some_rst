tests/reward-distribution/multipliers/default-multiplier-decimals.test.ts
=========================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { PublicKey } from "@solana/web3.js";
import { Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import { createStakePool, rewardDistributor } from "../../../src";
import { RewardDistributorKind } from "../../../src/programs/rewardDistributor";
import { getRewardDistributor } from "../../../src/programs/rewardDistributor/accounts";
import { findRewardDistributorId } from "../../../src/programs/rewardDistributor/pda";
import { createMint, executeTransaction } from "../../utils";
import type { CardinalProvider } from "../../workspace";
import { getProvider } from "../../workspace";

describe("Stake and claim rewards", () => {
  let provider: CardinalProvider;
  let rewardMintId: PublicKey;
  let stakePoolId: PublicKey;

  const maxSupply = 100;

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
    const transaction = new Transaction();
    await rewardDistributor.transaction.withInitRewardDistributor(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        rewardMintId: rewardMintId,
        kind: RewardDistributorKind.Treasury,
        maxSupply: new BN(maxSupply),
        defaultMultiplier: new BN(10),
        multiplierDecimals: 1,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const rewardDistributorData = await getRewardDistributor(
      provider.connection,
      rewardDistributorId
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      rewardMintId.toString()
    );
    expect(rewardDistributorData.parsed.defaultMultiplier.toNumber()).toEqual(
      10
    );
    expect(rewardDistributorData.parsed.multiplierDecimals).toEqual(1);
  });
});


