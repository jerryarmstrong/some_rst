tests/reward-distribution/stake-treasury-max-supply.test.ts
===========================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { executeTransactions, findAta, withWrapSol } from "@cardinal/common";
import { BN } from "@coral-xyz/anchor";
import { getAccount } from "@solana/spl-token";
import type { Keypair } from "@solana/web3.js";
import { LAMPORTS_PER_SOL, PublicKey, Transaction } from "@solana/web3.js";

import {
  claimRewards,
  createStakeEntryAndStakeMint,
  createStakePool,
  stake,
} from "../../src";
import { RewardDistributorKind } from "../../src/programs/rewardDistributor";
import { getRewardDistributor } from "../../src/programs/rewardDistributor/accounts";
import { findRewardDistributorId } from "../../src/programs/rewardDistributor/pda";
import { withInitRewardDistributor } from "../../src/programs/rewardDistributor/transaction";
import { ReceiptType } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMint, delay, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Stake and claim rewards from treasury", () => {
  const maxSupply = 5; // 5 wsol

  let provider: CardinalProvider;
  let stakePoolId: PublicKey;
  let stakeMintKeypair: Keypair | undefined;
  let originalMintId: PublicKey;
  const rewardMint = new PublicKey(
    "So11111111111111111111111111111111111111112"
  );
  let originalMintTokenAccountId: PublicKey;

  beforeAll(async () => {
    provider = await getProvider();
    // original mint
    [originalMintTokenAccountId, originalMintId] = await createMint(
      provider.connection,
      provider.wallet,
      { amount: 1 }
    );
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

    // wrapped sol to creator
    await withWrapSol(
      transaction,
      provider.connection,
      provider.wallet,
      maxSupply * LAMPORTS_PER_SOL
    );

    await withInitRewardDistributor(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        rewardMintId: rewardMint,
        rewardAmount: new BN(1 * LAMPORTS_PER_SOL),
        rewardDurationSeconds: new BN(2),
        kind: RewardDistributorKind.Treasury,
        maxSupply: new BN(maxSupply * LAMPORTS_PER_SOL),
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const rewardDistributorId = findRewardDistributorId(stakePoolId);

    const rewardDistributorData = await getRewardDistributor(
      provider.connection,
      rewardDistributorId
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      rewardMint.toString()
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      rewardMint.toString()
    );

    expect(rewardDistributorData.parsed.rewardMint.toString()).toEqual(
      rewardMint.toString()
    );
  });

  it("Init stake entry and mint", async () => {
    let transaction: Transaction;

    [transaction, , stakeMintKeypair] = await createStakeEntryAndStakeMint(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }
    );
    await executeTransaction(
      provider.connection,
      transaction,
      provider.wallet,
      { signers: stakeMintKeypair ? [stakeMintKeypair] : [] }
    );

    const stakeEntryData = await getStakeEntry(
      provider.connection,
      await findStakeEntryIdFromMint(
        provider.connection,
        provider.wallet.publicKey,
        stakePoolId,
        originalMintId
      )
    );

    expect(stakeEntryData.parsed.originalMint.toString()).toEqual(
      originalMintId.toString()
    );
    expect(stakeEntryData.parsed.pool.toString()).toEqual(
      stakePoolId.toString()
    );
    expect(stakeEntryData.parsed.stakeMint?.toString()).toEqual(
      stakeMintKeypair?.publicKey.toString()
    );
  });

  it("Stake", async () => {
    const transaction = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      userOriginalMintTokenAccountId: originalMintTokenAccountId,
      receiptType: ReceiptType.Receipt,
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

    if (stakeMintKeypair) {
      const userReceiptMintTokenAccountId = await findAta(
        stakeMintKeypair.publicKey,
        provider.wallet.publicKey,
        true
      );

      expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
      expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
        provider.wallet.publicKey.toString()
      );

      const checkUserReceiptMintTokenAccountId = await getAccount(
        provider.connection,
        userReceiptMintTokenAccountId
      );
      expect(Number(checkUserReceiptMintTokenAccountId.amount)).toEqual(1);
      expect(checkUserReceiptMintTokenAccountId.isFrozen).toEqual(true);
    }
  });

  it("Claim Rewards", async () => {
    await delay(6000);
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );

    const userRewardMintTokenAccountId = await findAta(
      rewardMint,
      provider.wallet.publicKey,
      true
    );

    let beforeAmount = 0;
    try {
      beforeAmount = Number(
        (await getAccount(provider.connection, userRewardMintTokenAccountId))
          .amount
      );
    } catch (e) {
      beforeAmount = 0;
    }

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

    const afterCheckUserRewardMintTokenAccountId = await getAccount(
      provider.connection,
      userRewardMintTokenAccountId
    );
    expect(Number(afterCheckUserRewardMintTokenAccountId.amount)).toEqual(
      beforeAmount + 3000000000
    );
  });
});


