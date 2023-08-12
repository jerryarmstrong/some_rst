tests/stake/resize-stake-entry.test.ts
======================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { beforeAll, expect } from "@jest/globals";
import { getAccount, getAssociatedTokenAddressSync } from "@solana/spl-token";
import type { PublicKey } from "@solana/web3.js";
import { SystemProgram, Transaction } from "@solana/web3.js";

import { createStakePool, stake } from "../../src";
import { ReceiptType, stakePoolProgram } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

let provider: CardinalProvider;
let originalMintTokenAccountId: PublicKey;
let originalMintId: PublicKey;
let stakePoolId: PublicKey;

describe("Resize stake entry", () => {
  beforeAll(async () => {
    provider = await getProvider();
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );
  });

  it("Create Pool", async () => {
    let tx: Transaction;
    [tx, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {}
    );
    await executeTransaction(provider.connection, tx, provider.wallet);
  });

  it("Stake", async () => {
    const tx = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      userOriginalMintTokenAccountId: originalMintTokenAccountId,
      receiptType: ReceiptType.Original,
    });
    await executeTransaction(provider.connection, tx, provider.wallet);

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

  it("Resize", async () => {
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId
    );

    const tx = new Transaction().add(
      await stakePoolProgram(provider.connection, provider.wallet)
        .methods.stakeEntryResize()
        .accounts({
          stakeEntry: stakeEntryId,
          payer: provider.wallet.publicKey,
          systemProgram: SystemProgram.programId,
        })
        .instruction()
    );
    await executeTransaction(provider.connection, tx, provider.wallet);
  });
});


