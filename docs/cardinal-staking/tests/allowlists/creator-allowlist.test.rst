tests/allowlists/creator-allowlist.test.ts
==========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findAta } from "@cardinal/common";
import { Wallet } from "@coral-xyz/anchor";
import { getAccount } from "@solana/spl-token";
import type { PublicKey, Transaction } from "@solana/web3.js";

import { createStakeEntry, createStakePool, stake } from "../../src";
import { ReceiptType } from "../../src/programs/stakePool";
import {
  getStakeEntry,
  getStakePool,
} from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import {
  createMasterEdition,
  executeTransaction,
  newAccountWithLamports,
} from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Creator allowlist", () => {
  let provider: CardinalProvider;
  const overlayText = "staking";
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  let originalMintAuthorityId: PublicKey;
  let stakePoolId: PublicKey;

  beforeAll(async () => {
    provider = await getProvider();
    // original mint
    const originalMintAuthority = await newAccountWithLamports(
      provider.connection
    );
    originalMintAuthorityId = originalMintAuthority.publicKey;
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      new Wallet(originalMintAuthority),
      { target: provider.wallet.publicKey }
    );
  });

  it("Create Pool", async () => {
    let transaction: Transaction;
    [transaction, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {
        overlayText: overlayText,
        requiresCreators: [originalMintAuthorityId],
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakePoolData = await getStakePool(provider.connection, stakePoolId);
    expect(stakePoolData.parsed.requiresCreators[0]?.toString()).toEqual(
      originalMintAuthorityId.toString()
    );
  });

  it("Init stake entry for pool", async () => {
    const [transaction, _] = await createStakeEntry(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }
    );
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

    expect(stakeEntryData.parsed.originalMint.toString()).toEqual(
      originalMintId.toString()
    );
    expect(stakeEntryData.parsed.pool.toString()).toEqual(
      stakePoolId.toString()
    );
    expect(stakeEntryData.parsed.stakeMint).toEqual(null);
  });

  it("Stake successs", async () => {
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
});


