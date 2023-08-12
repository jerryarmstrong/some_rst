tests/reward-distribution/multipliers/rewards-multiplier-test.test.ts
=====================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    // blockasset setup
import { executeTransactions, findAta } from "@cardinal/common";
import { getAccount } from "@solana/spl-token";
import type { PublicKey } from "@solana/web3.js";
import { Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import {
  claimRewards,
  createStakePool,
  initializeRewardEntry,
  stake,
} from "../../../src";
import {
  getRewardDistributor,
  getRewardEntry,
} from "../../../src/programs/rewardDistributor/accounts";
import {
  findRewardDistributorId,
  findRewardEntryId,
} from "../../../src/programs/rewardDistributor/pda";
import {
  withInitRewardDistributor,
  withUpdateRewardEntry,
} from "../../../src/programs/rewardDistributor/transaction";
import { getStakeEntry } from "../../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../../src/programs/stakePool/utils";
import { createMint, delay, executeTransaction } from "../../utils";
import type { CardinalProvider } from "../../workspace";
import { getProvider } from "../../workspace";

describe("Stake and claim rewards", () => {
  let provider: CardinalProvider;
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  let rewardMintId: PublicKey;
  let stakePoolId: PublicKey;
  let rewardDistributorId: PublicKey;

  // fungible test that the amount and seconds should be zero
  beforeAll(async () => {
    provider = await getProvider();
    // original mint
    [originalMintTokenAccountId, originalMintId] = await createMint(
      provider.connection,
      provider.wallet,
      { amount: 1, decimals: 6 }
    );

    // reward mint
    [, rewardMintId] = await createMint(provider.connection, provider.wallet, {
      amount: 0,
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

    await withInitRewardDistributor(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        rewardMintId: rewardMintId,
        rewardAmount: new BN((10 ** 6 / 24 / 60 / 60) * 1000),
        rewardDurationSeconds: new BN(1),
        supply: new BN(5 * 10 * 6),
        defaultMultiplier: new BN(1000),
        multiplierDecimals: 7,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    rewardDistributorId = findRewardDistributorId(stakePoolId);
    const rewardDistributorData = await getRewardDistributor(
      provider.connection,
      rewardDistributorId
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      rewardMintId.toString()
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      rewardMintId.toString()
    );
  });

  it("Create Reward Entry", async () => {
    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );

    const transaction = await initializeRewardEntry(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }
    );

    await withUpdateRewardEntry(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        rewardDistributorId: rewardDistributorId,
        stakeEntryId: stakeEntryId,
        multiplier: new BN(12481),
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardEntryId = findRewardEntryId(rewardDistributorId, stakeEntryId);

    const rewardEntryData = await getRewardEntry(
      provider.connection,
      rewardEntryId
    );

    expect(rewardEntryData.parsed.rewardDistributor.toString()).toEqual(
      rewardDistributorId.toString()
    );

    expect(rewardEntryData.parsed.stakeEntry.toString()).toEqual(
      stakeEntryId.toString()
    );
  });

  it("Stake", async () => {
    const transaction = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      userOriginalMintTokenAccountId: originalMintTokenAccountId,
    });
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeEntryData = await getStakeEntry(
      provider.connection,
      await findStakeEntryIdFromMint(
        provider.connection,
        provider.wallet.publicKey,
        stakePoolId,
        originalMintId
      )
    );

    const userOriginalMintTokenAccountId = await findAta(
      originalMintId,
      provider.wallet.publicKey,
      true
    );

    expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );

    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(0);
  });

  it("Claim Rewards", async () => {
    await delay(4000);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );

    const rewardEntryId = findRewardEntryId(rewardDistributorId, stakeEntryId);

    const transactions = await claimRewards(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        stakeEntryIds: [stakeEntryId],
      }
    );
    await executeTransactions(
      provider.connection,
      transactions,
      provider.wallet
    );

    const userOriginalMintTokenAccountId = await findAta(
      originalMintId,
      provider.wallet.publicKey,
      true
    );
    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(0);

    const rewardEntryAfter = await getRewardEntry(
      provider.connection,
      rewardEntryId
    );

    const userRewardMintTokenAccount = await findAta(
      rewardMintId,
      provider.wallet.publicKey,
      true
    );

    const rewardDistributorData = await getRewardDistributor(
      provider.connection,
      rewardDistributorId
    );
    const a = await getAccount(provider.connection, userRewardMintTokenAccount);
    console.log("user reward mint token acount", Number(a.amount));
    console.log(
      "rewardsIssued",
      rewardDistributorData.parsed.rewardsIssued.toNumber()
    );

    expect(
      rewardEntryAfter.parsed.rewardSecondsReceived.toNumber()
    ).toBeGreaterThan(0);
  });
});


