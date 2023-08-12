tests/reward-distribution/stake-permissionless-claim-rewards.test.ts
====================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { executeTransactions, findAta } from "@cardinal/common";
import { Wallet } from "@coral-xyz/anchor";
import { getAccount } from "@solana/spl-token";
import {
  Keypair,
  LAMPORTS_PER_SOL,
  PublicKey,
  Transaction,
} from "@solana/web3.js";

import {
  claimRewards,
  createStakePool,
  initializeRewardEntry,
  stake,
  unstake,
} from "../../src";
import {
  getRewardDistributor,
  getRewardEntry,
} from "../../src/programs/rewardDistributor/accounts";
import {
  findRewardDistributorId,
  findRewardEntryId,
} from "../../src/programs/rewardDistributor/pda";
import { withInitRewardDistributor } from "../../src/programs/rewardDistributor/transaction";
import { ReceiptType } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import {
  createMasterEdition,
  createMint,
  delay,
  executeTransaction,
} from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Stake and claim permissionless rewards", () => {
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  let rewardMintId: PublicKey;
  let stakePoolId: PublicKey;
  let provider: CardinalProvider;

  const rewardClaimer = Keypair.generate();

  beforeAll(async () => {
    provider = await getProvider();
    // original mint
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );

    // original mint
    [, rewardMintId] = await createMint(provider.connection, provider.wallet, {
      amount: 0,
    });

    const fromAirdropSignature = await provider.connection.requestAirdrop(
      rewardClaimer.publicKey,
      10 * LAMPORTS_PER_SOL
    );
    await provider.connection.confirmTransaction(fromAirdropSignature);
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
      receiptType: ReceiptType.Original,
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
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(true);
  });

  it("Claim Rewards fail", async () => {
    await delay(2000);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );

    const [transaction] = await claimRewards(
      provider.connection,
      new Wallet(rewardClaimer),
      {
        stakePoolId: stakePoolId,
        stakeEntryIds: [stakeEntryId],
      }
    );
    await expect(
      executeTransaction(provider.connection, transaction!, provider.wallet, {
        silent: true,
      })
    ).rejects.toThrow();
  });

  it("Claim Rewards", async () => {
    await delay(2000);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );
    const oldStakeEntryData = await getStakeEntry(
      provider.connection,
      stakeEntryId
    );

    const transactions = await claimRewards(
      provider.connection,
      new Wallet(rewardClaimer),
      {
        stakePoolId: stakePoolId,
        stakeEntryIds: [stakeEntryId],
        lastStaker: oldStakeEntryData.parsed.lastStaker,
      }
    );
    await executeTransactions(
      provider.connection,
      transactions,
      new Wallet(rewardClaimer)
    );

    const newStakeEntryData = await getStakeEntry(
      provider.connection,
      stakeEntryId
    );
    expect(newStakeEntryData.parsed.lastUpdatedAt).not.toEqual(null);
    expect(oldStakeEntryData.parsed.lastUpdatedAt).not.toEqual(null);
    expect(newStakeEntryData.parsed.lastUpdatedAt?.toNumber()).toBeGreaterThan(
      oldStakeEntryData.parsed.lastUpdatedAt?.toNumber() ?? 0
    );
    expect(newStakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(newStakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(
      newStakeEntryData.parsed.totalStakeSeconds.toNumber()
    ).toBeGreaterThan(oldStakeEntryData.parsed.totalStakeSeconds.toNumber());

    const userRewardMintTokenAccountId = await findAta(
      rewardMintId,
      provider.wallet.publicKey,
      true
    );

    const checkUserRewardTokenAccount = await getAccount(
      provider.connection,
      userRewardMintTokenAccountId
    );
    expect(Number(checkUserRewardTokenAccount.amount)).toBeGreaterThan(1);

    const userOriginalMintTokenAccountId = await findAta(
      originalMintId,
      provider.wallet.publicKey,
      true
    );
    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(true);
  });

  it("Unstake", async () => {
    const transaction = await unstake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
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
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      PublicKey.default.toString()
    );
    expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);

    const userOriginalMintTokenAccountId = await findAta(
      originalMintId,
      provider.wallet.publicKey,
      true
    );
    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(false);

    const stakeEntryOriginalMintTokenAccountId = await findAta(
      originalMintId,
      stakeEntryData.pubkey,
      true
    );

    const userRewardMintTokenAccountId = await findAta(
      rewardMintId,
      provider.wallet.publicKey,
      true
    );

    const checkStakeEntryOriginalMintTokenAccount = await getAccount(
      provider.connection,
      stakeEntryOriginalMintTokenAccountId
    );
    expect(Number(checkStakeEntryOriginalMintTokenAccount.amount)).toEqual(0);

    const checkUserRewardTokenAccount = await getAccount(
      provider.connection,
      userRewardMintTokenAccountId
    );
    expect(Number(checkUserRewardTokenAccount.amount)).toBeGreaterThan(1);
  });
});


