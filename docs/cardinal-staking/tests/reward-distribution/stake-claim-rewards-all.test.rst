tests/reward-distribution/stake-claim-rewards-all.test.ts
=========================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import {
  createMint,
  executeTransactionSequence,
  newAccountWithLamports,
  tryNull,
} from "@cardinal/common";
import { Wallet } from "@coral-xyz/anchor";
import { beforeAll, expect, test } from "@jest/globals";
import {
  createAssociatedTokenAccountIdempotentInstruction,
  createTransferInstruction,
  getAccount,
  getAssociatedTokenAddressSync,
} from "@solana/spl-token";
import { PublicKey, Transaction } from "@solana/web3.js";

import {
  claimRewardsAll,
  createStakePool,
  stakeAll,
  unstakeAll,
} from "../../src";
import { getRewardDistributor } from "../../src/programs/rewardDistributor/accounts";
import { findRewardDistributorId } from "../../src/programs/rewardDistributor/pda";
import { withInitRewardDistributor } from "../../src/programs/rewardDistributor/transaction";
import { ReceiptType } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

let provider: CardinalProvider;
const originalMintTokenAccountIds: PublicKey[] = [];
const originalMintIds: PublicKey[] = [];
let rewardMintId: PublicKey;
let mintAuthorityRewardMintTokenAccountId: PublicKey;
let stakePoolId: PublicKey;
let mintAuthority: Wallet;
const REWARD_MINT_SUPPLY = 100;

describe("Stake unstake", () => {
  beforeAll(async () => {
    provider = await getProvider();
    mintAuthority = new Wallet(
      await newAccountWithLamports(provider.connection)
    );
    const [ata1, mint1] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );
    originalMintIds.push(mint1);
    originalMintTokenAccountIds.push(ata1);
    const [ata2, mint2] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );
    originalMintIds.push(mint2);
    originalMintTokenAccountIds.push(ata2);
    const [ata3, mint3] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );
    originalMintIds.push(mint3);
    originalMintTokenAccountIds.push(ata3);

    [mintAuthorityRewardMintTokenAccountId, rewardMintId] = await createMint(
      provider.connection,
      mintAuthority,
      {
        amount: REWARD_MINT_SUPPLY,
      }
    );
  });

  test("Create Pool", async () => {
    let transaction: Transaction;
    [transaction, stakePoolId] = await createStakePool(
      provider.connection,
      mintAuthority,
      {}
    );
    await executeTransaction(provider.connection, transaction, mintAuthority);
  });

  it("Create Reward Distributor", async () => {
    const transaction = new Transaction();
    await withInitRewardDistributor(
      transaction,
      provider.connection,
      mintAuthority,
      {
        stakePoolId: stakePoolId,
        rewardMintId: rewardMintId,
      }
    );
    await executeTransaction(provider.connection, transaction, mintAuthority);

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

  it("Add funds", async () => {
    const rewardDistributorId = findRewardDistributorId(stakePoolId);
    const transaction = new Transaction();
    const rewardDistributorTokenAccountId = getAssociatedTokenAddressSync(
      rewardMintId,
      rewardDistributorId,
      true
    );
    transaction.add(
      createAssociatedTokenAccountIdempotentInstruction(
        mintAuthority.publicKey,
        rewardDistributorTokenAccountId,
        rewardDistributorId,
        rewardMintId
      )
    );
    transaction.add(
      createTransferInstruction(
        mintAuthorityRewardMintTokenAccountId,
        rewardDistributorTokenAccountId,
        mintAuthority.publicKey,
        REWARD_MINT_SUPPLY
      )
    );
    await executeTransaction(provider.connection, transaction, mintAuthority);
    const checkRewardDistributorTokenAccount = await getAccount(
      provider.connection,
      rewardDistributorTokenAccountId
    );
    expect(Number(checkRewardDistributorTokenAccount.amount)).toEqual(
      REWARD_MINT_SUPPLY
    );
  });

  test("Stake", async () => {
    const txs = await stakeAll(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      mintInfos: originalMintIds.map((mintId, i) => ({
        mintId,
        tokenAccountId: originalMintTokenAccountIds[i]!,
        receiptType: ReceiptType.Original,
      })),
    });
    await executeTransactionSequence(provider.connection, txs, provider.wallet);

    for (const originalMintId of originalMintIds) {
      const stakeEntryData = await getStakeEntry(
        provider.connection,
        await findStakeEntryIdFromMint(
          provider.connection,
          provider.wallet.publicKey,
          stakePoolId,
          originalMintId
        )
      );

      expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
      expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
        provider.wallet.publicKey.toString()
      );

      const checkUserOriginalTokenAccount = await getAccount(
        provider.connection,
        getAssociatedTokenAddressSync(
          originalMintId,
          provider.wallet.publicKey,
          true
        )
      );
      expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
      expect(checkUserOriginalTokenAccount.isFrozen).toEqual(true);
    }
  });

  test("Claim rewards", async () => {
    const userRewardTokenAccountId = getAssociatedTokenAddressSync(
      rewardMintId,
      provider.wallet.publicKey,
      true
    );
    const useRewardTokenAccountBefore = await tryNull(
      getAccount(provider.connection, userRewardTokenAccountId)
    );

    await new Promise((r) => setTimeout(r, 2000));
    const stakeEntryIds = await Promise.all(
      originalMintIds.map(
        async (mintId) =>
          await findStakeEntryIdFromMint(
            provider.connection,
            provider.wallet.publicKey,
            stakePoolId,
            mintId,
            false
          )
      )
    );
    const txs = await claimRewardsAll(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      stakeEntryIds,
    });
    await executeTransactionSequence(provider.connection, txs, provider.wallet);

    for (const originalMintId of originalMintIds) {
      const stakeEntryData = await getStakeEntry(
        provider.connection,
        await findStakeEntryIdFromMint(
          provider.connection,
          provider.wallet.publicKey,
          stakePoolId,
          originalMintId
        )
      );
      expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
      expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
        provider.wallet.publicKey.toString()
      );

      const checkUserOriginalTokenAccount = await getAccount(
        provider.connection,
        getAssociatedTokenAddressSync(
          originalMintId,
          provider.wallet.publicKey,
          true
        )
      );
      expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);
      expect(checkUserOriginalTokenAccount.isFrozen).toEqual(true);

      const checkUserRewardTokenAccount = await getAccount(
        provider.connection,
        userRewardTokenAccountId
      );
      expect(Number(checkUserRewardTokenAccount.amount)).toBeGreaterThan(
        Number(useRewardTokenAccountBefore?.amount ?? 0)
      );
    }
  });

  test("Unstake", async () => {
    const userRewardTokenAccountId = getAssociatedTokenAddressSync(
      rewardMintId,
      provider.wallet.publicKey,
      true
    );
    const useRewardTokenAccountBefore = await tryNull(
      getAccount(provider.connection, userRewardTokenAccountId)
    );
    await new Promise((r) => setTimeout(r, 2000));
    const txs = await unstakeAll(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      mintInfos: originalMintIds.map((mintId) => ({ mintId })),
    });
    await executeTransactionSequence(provider.connection, txs, provider.wallet);
    for (const originalMintId of originalMintIds) {
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

      const userOriginalMintTokenAccountId = getAssociatedTokenAddressSync(
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

      const checkUserRewardTokenAccount = await getAccount(
        provider.connection,
        userRewardTokenAccountId
      );
      expect(Number(checkUserRewardTokenAccount.amount)).toBeGreaterThan(
        Number(useRewardTokenAccountBefore?.amount ?? 0)
      );
    }
  });
});


