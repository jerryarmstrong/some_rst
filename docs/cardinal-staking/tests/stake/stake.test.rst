tests/stake/stake.test.ts
=========================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { beforeAll, expect, test } from "@jest/globals";
import { getAccount, getAssociatedTokenAddressSync } from "@solana/spl-token";
import type { Transaction } from "@solana/web3.js";
import { PublicKey } from "@solana/web3.js";

import { createStakePool, stake, unstake } from "../../src";
import { ReceiptType } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

let provider: CardinalProvider;
let originalMintTokenAccountId: PublicKey;
let originalMintId: PublicKey;
let stakePoolId: PublicKey;

describe("Stake unstake", () => {
  beforeAll(async () => {
    provider = await getProvider();
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );
  });

  test("Create Pool", async () => {
    let transaction: Transaction;
    [transaction, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {}
    );

    await executeTransaction(provider.connection, transaction, provider.wallet);
  });

  test("Stake", async () => {
    await executeTransaction(
      provider.connection,
      await stake(provider.connection, provider.wallet, {
        stakePoolId: stakePoolId,
        originalMintId,
        userOriginalMintTokenAccountId: originalMintTokenAccountId,
        receiptType: ReceiptType.Original,
      }),
      provider.wallet
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

  test("Unstake", async () => {
    await executeTransaction(
      provider.connection,
      await unstake(provider.connection, provider.wallet, {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }),
      provider.wallet
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


