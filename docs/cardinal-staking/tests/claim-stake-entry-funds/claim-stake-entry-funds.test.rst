tests/claim-stake-entry-funds/claim-stake-entry-funds.test.ts
=============================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import {
  createMint,
  findAta,
  withFindOrInitAssociatedTokenAccount,
} from "@cardinal/common";
import { beforeAll, expect, test } from "@jest/globals";
import {
  createTransferCheckedInstruction,
  getAccount,
  getAssociatedTokenAddressSync,
} from "@solana/spl-token";
import type { PublicKey } from "@solana/web3.js";
import { Transaction } from "@solana/web3.js";

import { createStakePool, stake } from "../../src";
import { ReceiptType } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryId } from "../../src/programs/stakePool/pda";
import { withClaimStakeEntryFunds } from "../../src/programs/stakePool/transaction";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

let provider: CardinalProvider;
let originalMintTokenAccountId: PublicKey;
let originalMintId: PublicKey;
let stakePoolId: PublicKey;
let customPaymentMint: PublicKey;

const initialSupply = 100000;
const transferAmount = 100;

describe("Claim stake entry funds", () => {
  beforeAll(async () => {
    provider = await getProvider();
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );
    [, customPaymentMint] = await createMint(
      provider.connection,
      provider.wallet,
      { amount: initialSupply }
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

  test("Sends funds to stake entry", async () => {
    const transaction = new Transaction();
    const stakeEntryId = findStakeEntryId(
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId,
      false
    );

    const stakeEntryAtaId = await withFindOrInitAssociatedTokenAccount(
      transaction,
      provider.connection,
      customPaymentMint,
      stakeEntryId,
      provider.wallet.publicKey,
      true
    );
    const authorityAtaId = await findAta(
      customPaymentMint,
      provider.wallet.publicKey,
      true
    );

    transaction.add(
      createTransferCheckedInstruction(
        authorityAtaId,
        customPaymentMint,
        stakeEntryAtaId,
        provider.wallet.publicKey,
        transferAmount,
        0
      )
    );

    await executeTransaction(provider.connection, transaction, provider.wallet);

    const accountInfo = await getAccount(provider.connection, stakeEntryAtaId);
    expect(accountInfo.amount.toString()).toEqual(transferAmount.toString());
  });

  test("Claim funds from stake entry", async () => {
    const transaction = new Transaction();
    const stakeEntryId = findStakeEntryId(
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId,
      false
    );
    const authorityAtaId = await findAta(
      customPaymentMint,
      provider.wallet.publicKey,
      true
    );
    const beforeAccountData = await getAccount(
      provider.connection,
      authorityAtaId
    );
    expect(beforeAccountData.amount.toString()).toEqual(
      (initialSupply - transferAmount).toString()
    );

    await withClaimStakeEntryFunds(
      transaction,
      provider.connection,
      provider.wallet,
      stakeEntryId,
      customPaymentMint
    );

    await executeTransaction(provider.connection, transaction, provider.wallet);

    const afterAccountData = await getAccount(
      provider.connection,
      authorityAtaId
    );
    expect(afterAccountData.amount.toString()).toEqual(
      initialSupply.toString()
    );
  });
});


