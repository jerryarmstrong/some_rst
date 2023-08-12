tests/reward-distribution/create-entry-close-pool.test.ts
=========================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { tryGetAccount } from "@cardinal/common";
import type { PublicKey } from "@solana/web3.js";
import { Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import {
  createStakeEntry,
  createStakePool,
  rewardDistributor,
  stake,
  unstake,
} from "../../src";
import { RewardDistributorKind } from "../../src/programs/rewardDistributor";
import { getRewardDistributor } from "../../src/programs/rewardDistributor/accounts";
import { findRewardDistributorId } from "../../src/programs/rewardDistributor/pda";
import {
  getStakeEntry,
  getStakePool,
} from "../../src/programs/stakePool/accounts";
import {
  withCloseStakeEntry,
  withCloseStakePool,
} from "../../src/programs/stakePool/transaction";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEdition, createMint, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Stake and claim rewards", () => {
  let provider: CardinalProvider;
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  let rewardMintId: PublicKey;
  let stakePoolId: PublicKey;

  const maxSupply = 100;

  beforeAll(async () => {
    provider = await getProvider();
    // original mint
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );

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
        defaultMultiplier: new BN(1),
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
      1
    );
    expect(rewardDistributorData.parsed.multiplierDecimals).toEqual(1);
  });

  it("Create Stake And Reward Entry", async () => {
    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const [transaction, stakeEntryId] = await createStakeEntry(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }
    );
    await rewardDistributor.transaction.withInitRewardEntry(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakeEntryId: stakeEntryId,
        rewardDistributorId: rewardDistributorId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardDistributorData = await getRewardDistributor(
      provider.connection,
      rewardDistributorId
    );
    expect(rewardDistributorData.parsed.defaultMultiplier.toNumber()).toEqual(
      1
    );
  });

  test("Stake", async () => {
    await executeTransaction(
      provider.connection,
      await stake(provider.connection, provider.wallet, {
        stakePoolId: stakePoolId,
        originalMintId,
        userOriginalMintTokenAccountId: originalMintTokenAccountId,
      }),
      provider.wallet
    );
  });

  it("Fail close pool", async () => {
    const transaction = await withCloseStakePool(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
      }
    );
    await expect(
      executeTransaction(provider.connection, transaction, provider.wallet, {
        silent: true,
      })
    ).rejects.toThrow();
  });

  test("Unstake", async () => {
    await executeTransaction(
      provider.connection,
      await unstake(provider.connection, provider.wallet, {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }),
      provider.wallet
    );
  });

  it("Close entry then pool", async () => {
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );
    const transaction = new Transaction();
    await withCloseStakeEntry(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        stakeEntryId: stakeEntryId,
      }
    );
    await withCloseStakePool(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeEntry = await tryGetAccount(() =>
      getStakeEntry(provider.connection, stakeEntryId)
    );
    expect(stakeEntry).toEqual(null);

    const stakePool = await tryGetAccount(() =>
      getStakePool(provider.connection, stakePoolId)
    );
    expect(stakePool).toEqual(null);
  });
});


