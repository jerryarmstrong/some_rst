tests/stake/stake-unstake-all.test.ts
=====================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { executeTransactionSequence } from "@cardinal/common";
import { beforeAll, expect, test } from "@jest/globals";
import { getAccount, getAssociatedTokenAddressSync } from "@solana/spl-token";
import type { Transaction } from "@solana/web3.js";
import { PublicKey } from "@solana/web3.js";

import { createStakePool, stakeAll, unstakeAll } from "../../src";
import { ReceiptType } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

let provider: CardinalProvider;
const originalMintTokenAccountIds: PublicKey[] = [];
const originalMintIds: PublicKey[] = [];

let stakePoolId: PublicKey;

describe("Stake unstake", () => {
  beforeAll(async () => {
    provider = await getProvider();
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
    }
  });

  test("Unstake", async () => {
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
    }
  });
});


