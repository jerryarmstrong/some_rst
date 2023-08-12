tests/reward-distribution/reclaim-funds.test.ts
===============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findAta } from "@cardinal/common";
import { getAccount } from "@solana/spl-token";
import * as web3 from "@solana/web3.js";
import { BN } from "bn.js";

import { createRewardDistributor, createStakePool } from "../../src";
import { RewardDistributorKind } from "../../src/programs/rewardDistributor";
import { getRewardDistributor } from "../../src/programs/rewardDistributor/accounts";
import { findRewardDistributorId } from "../../src/programs/rewardDistributor/pda";
import { withReclaimFunds } from "../../src/programs/rewardDistributor/transaction";
import { createMint, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Reclaim funds", () => {
  const maxSupply = 100;
  let provider: CardinalProvider;
  let stakePoolId: web3.PublicKey;
  let rewardMintId: web3.PublicKey;

  beforeAll(async () => {
    provider = await getProvider();
    provider = await getProvider();
    // reward mint
    [, rewardMintId] = await createMint(provider.connection, provider.wallet, {
      amount: maxSupply,
    });
  });

  it("Create Pool", async () => {
    let transaction: web3.Transaction;
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

  it("Reclaim funds", async () => {
    const transaction = new web3.Transaction();

    await withReclaimFunds(transaction, provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      amount: new BN(50),
    });
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const rewardDistributorData = await getRewardDistributor(
      provider.connection,
      rewardDistributorId
    );
    const rewardDistributorTokenAccountId = await findAta(
      rewardDistributorData.parsed.rewardMint,
      rewardDistributorId,
      true
    );
    const rewardDistributorTokenAccount = await getAccount(
      provider.connection,
      rewardDistributorTokenAccountId
    );

    expect(Number(rewardDistributorTokenAccount.amount)).toEqual(50);
  });
});


