tests/stake/stake-pool-count.test.ts
====================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { beforeAll, expect } from "@jest/globals";
import { getAccount, getAssociatedTokenAddressSync } from "@solana/spl-token";
import type { Transaction } from "@solana/web3.js";
import { PublicKey } from "@solana/web3.js";

import { createStakePool, stake, unstake } from "../../src";
import { ReceiptType } from "../../src/programs/stakePool";
import {
  getActiveStakeEntriesForPool,
  getAllStakePools,
  getStakeEntry,
} from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

let provider: CardinalProvider;
let originalMintTokenAccountId: PublicKey;
let originalMintId: PublicKey;
let stakePoolId: PublicKey;

describe("Stake pool count", () => {
  beforeAll(async () => {
    provider = await getProvider();
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );
  });

  it("Create Pool", async () => {
    const stakePoolDatasBefore = await getAllStakePools(provider.connection);

    let transaction: Transaction;
    [transaction, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {}
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakePoolDatasAfter = await getAllStakePools(provider.connection);
    expect(stakePoolDatasAfter.length - 1).toEqual(stakePoolDatasBefore.length);
  });

  it("Stake", async () => {
    const activeStakeEntriesBefore = await getActiveStakeEntriesForPool(
      provider.connection,
      stakePoolId
    );
    const transaction = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      userOriginalMintTokenAccountId: originalMintTokenAccountId,
      receiptType: ReceiptType.Original,
    });
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const activeStakeEntriesAfter = await getActiveStakeEntriesForPool(
      provider.connection,
      stakePoolId
    );
    expect(activeStakeEntriesAfter.length - 1).toEqual(
      activeStakeEntriesBefore.length
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

    const userOriginalMintTokenAccountId = getAssociatedTokenAddressSync(
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

  it("Unstake", async () => {
    const activeStakeEntriesBefore = await getActiveStakeEntriesForPool(
      provider.connection,
      stakePoolId
    );

    const transaction = await unstake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
    });
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const activeStakeEntriesAfter = await getActiveStakeEntriesForPool(
      provider.connection,
      stakePoolId
    );
    expect(activeStakeEntriesBefore.length - 1).toEqual(
      activeStakeEntriesAfter.length
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
  });
});


