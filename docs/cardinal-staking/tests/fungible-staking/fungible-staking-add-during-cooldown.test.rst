tests/fungible-staking/fungible-staking-add-during-cooldown.test.ts
===================================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findAta } from "@cardinal/common";
import { BN, Wallet } from "@coral-xyz/anchor";
import { getAccount } from "@solana/spl-token";
import type { PublicKey, Transaction } from "@solana/web3.js";

import { createStakePool, stake, unstake } from "../../src";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import {
  createMint,
  executeTransaction,
  newAccountWithLamports,
} from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Fungible staking add during cooldown", () => {
  let provider: CardinalProvider;
  let stakePoolId: PublicKey;
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;

  const stakingAmount = 10;

  beforeAll(async () => {
    provider = await getProvider();
    // original mint
    const mintAuthority = await newAccountWithLamports(provider.connection);
    [originalMintTokenAccountId, originalMintId] = await createMint(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey, amount: stakingAmount }
    );
  });

  it("Create Pool", async () => {
    let transaction: Transaction;
    [transaction, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {
        cooldownSeconds: 10,
      }
    );

    await executeTransaction(provider.connection, transaction, provider.wallet);
  });

  it("Stake half", async () => {
    const transaction = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      userOriginalMintTokenAccountId: originalMintTokenAccountId,
      amount: new BN(stakingAmount / 2),
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

    const stakeEntryOriginalMintTokenAccountId = await findAta(
      originalMintId,
      stakeEntryData.pubkey,
      true
    );

    expect(stakeEntryData.parsed.amount.toNumber()).toEqual(stakingAmount / 2);
    expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );

    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(
      stakingAmount / 2
    );

    const checkStakeEntryOriginalMintTokenAccount = await getAccount(
      provider.connection,
      stakeEntryOriginalMintTokenAccountId
    );
    expect(Number(checkStakeEntryOriginalMintTokenAccount.amount)).toEqual(
      stakingAmount / 2
    );
  });

  it("Unstake", async () => {
    const transaction = await unstake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      fungible: true,
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

    const stakeEntryOriginalMintTokenAccountId = await findAta(
      originalMintId,
      stakeEntryData.pubkey,
      true
    );
    expect(
      stakeEntryData.parsed.cooldownStartSeconds?.toNumber()
    ).toBeGreaterThan(0);
    expect(stakeEntryData.parsed.amount.toNumber()).toEqual(stakingAmount / 2);
    expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );

    const checkUserOriginalTokenAccount = await getAccount(
      provider.connection,
      userOriginalMintTokenAccountId
    );
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(
      stakingAmount / 2
    );

    const checkStakeEntryOriginalMintTokenAccount = await getAccount(
      provider.connection,
      stakeEntryOriginalMintTokenAccountId
    );
    expect(Number(checkStakeEntryOriginalMintTokenAccount.amount)).toEqual(
      stakingAmount / 2
    );
  });
});


