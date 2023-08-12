tests/receipt-manager/receipt-manager-update-close.test.ts
==========================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { tryGetAccount } from "@cardinal/common";
import { getPaymentManager } from "@cardinal/payment-manager/dist/cjs/accounts";
import { findPaymentManagerAddress } from "@cardinal/payment-manager/dist/cjs/pda";
import { withInit } from "@cardinal/payment-manager/dist/cjs/transaction";
import { BN, Wallet } from "@coral-xyz/anchor";
import { Keypair, PublicKey, Transaction } from "@solana/web3.js";

import { createStakePool } from "../../src";
import { RECEIPT_MANAGER_PAYMENT_MANAGER_NAME } from "../../src/programs/receiptManager";
import { getReceiptManager } from "../../src/programs/receiptManager/accounts";
import { findReceiptManagerId } from "../../src/programs/receiptManager/pda";
import {
  withCloseReceiptManager,
  withInitReceiptManager,
  withUpdateReceiptManager,
} from "../../src/programs/receiptManager/transaction";
import { executeTransaction, newAccountWithLamports } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Create update close receipt manager", () => {
  let provider: CardinalProvider;
  let stakePoolId: PublicKey;
  let invalidAuthority: Keypair;

  const receiptManagerName = `mgr-${Math.random()}`;
  const requiredStakeSeconds = new BN(5);
  const stakeSecondsToUse = new BN(1);
  const updatedStakeSecondsToUse = new BN(10);
  const requiresAuthorization = false;

  const MAKER_FEE = 0;
  const TAKER_FEE = 0;
  const feeCollector = Keypair.generate();
  const paymentRecipient = Keypair.generate();
  const paymentMint = new PublicKey(
    "So11111111111111111111111111111111111111112"
  );

  beforeAll(async () => {
    provider = await getProvider();
    invalidAuthority = await newAccountWithLamports(provider.connection);
  });

  it("Create payment manager", async () => {
    const transaction = new Transaction();

    const [paymentManagerId] = await findPaymentManagerAddress(
      RECEIPT_MANAGER_PAYMENT_MANAGER_NAME
    );
    const checkIfPaymentManagerExists = await tryGetAccount(() =>
      getPaymentManager(provider.connection, paymentManagerId)
    );
    if (!checkIfPaymentManagerExists) {
      await withInit(
        transaction,
        provider.connection,
        provider.wallet,
        RECEIPT_MANAGER_PAYMENT_MANAGER_NAME,
        feeCollector.publicKey,
        MAKER_FEE,
        TAKER_FEE,
        false
      );
      await executeTransaction(
        provider.connection,
        transaction,
        provider.wallet
      );
    }

    const paymentManagerData = await getPaymentManager(
      provider.connection,
      paymentManagerId
    );
    expect(paymentManagerData.parsed.name).toEqual(
      RECEIPT_MANAGER_PAYMENT_MANAGER_NAME
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

  it("Invalid authority", async () => {
    const transaction = new Transaction();
    await withInitReceiptManager(
      transaction,
      provider.connection,
      provider.wallet,
      {
        name: receiptManagerName,
        stakePoolId: stakePoolId,
        authority: invalidAuthority.publicKey,
        requiredStakeSeconds: requiredStakeSeconds,
        stakeSecondsToUse: stakeSecondsToUse,
        paymentMint: paymentMint,
        paymentRecipientId: paymentRecipient.publicKey,
        requiresAuthorization: requiresAuthorization,
      }
    );
    await expect(
      executeTransaction(
        provider.connection,
        transaction,
        new Wallet(invalidAuthority),
        {
          silent: true,
        }
      )
    ).rejects.toThrow();
  });

  it("Create Reward Receipt Manager", async () => {
    const transaction = new Transaction();
    const [, receiptManagerId] = await withInitReceiptManager(
      transaction,
      provider.connection,
      provider.wallet,
      {
        name: receiptManagerName,
        stakePoolId: stakePoolId,
        authority: provider.wallet.publicKey,
        requiredStakeSeconds: requiredStakeSeconds,
        stakeSecondsToUse: stakeSecondsToUse,
        paymentMint: paymentMint,
        paymentRecipientId: paymentRecipient.publicKey,
        requiresAuthorization: requiresAuthorization,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const receiptManagerData = await getReceiptManager(
      provider.connection,
      receiptManagerId
    );
    const [payamentManagerId] = await findPaymentManagerAddress(
      RECEIPT_MANAGER_PAYMENT_MANAGER_NAME
    );
    expect(receiptManagerData.parsed.paymentManager.toString()).toEqual(
      payamentManagerId.toString()
    );
    expect(receiptManagerData.parsed.authority.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(receiptManagerData.parsed.paymentMint.toString()).toEqual(
      paymentMint.toString()
    );
    expect(receiptManagerData.parsed.stakePool.toString()).toEqual(
      stakePoolId.toString()
    );
    expect(receiptManagerData.parsed.requiredStakeSeconds.toString()).toEqual(
      requiredStakeSeconds.toString()
    );
    expect(receiptManagerData.parsed.stakeSecondsToUse.toString()).toEqual(
      stakeSecondsToUse.toString()
    );
    expect(receiptManagerData.parsed.requiresAuthorization.toString()).toEqual(
      requiresAuthorization.toString()
    );
  });

  it("Invalid authority updated", async () => {
    const transaction = new Transaction();
    await withUpdateReceiptManager(
      transaction,
      provider.connection,
      new Wallet(invalidAuthority),
      {
        name: receiptManagerName,
        stakePoolId: stakePoolId,
        authority: invalidAuthority.publicKey,
        requiredStakeSeconds: requiredStakeSeconds,
        stakeSecondsToUse: stakeSecondsToUse,
        paymentMint: paymentMint,
        paymentRecipientId: paymentRecipient.publicKey,
        requiresAuthorization: requiresAuthorization,
      }
    );
    await expect(
      executeTransaction(
        provider.connection,
        transaction,
        new Wallet(invalidAuthority),
        { silent: true }
      )
    ).rejects.toThrow();
  });

  it("Update reward receipt manager", async () => {
    const transaction = new Transaction();
    const [, receiptManagerId] = await withUpdateReceiptManager(
      transaction,
      provider.connection,
      provider.wallet,
      {
        name: receiptManagerName,
        stakePoolId: stakePoolId,
        authority: provider.wallet.publicKey,
        requiredStakeSeconds: requiredStakeSeconds,
        stakeSecondsToUse: updatedStakeSecondsToUse,
        paymentMint: paymentMint,
        paymentRecipientId: paymentRecipient.publicKey,
        requiresAuthorization: requiresAuthorization,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const receiptManagerData = await getReceiptManager(
      provider.connection,
      receiptManagerId
    );
    const [payamentManagerId] = await findPaymentManagerAddress(
      RECEIPT_MANAGER_PAYMENT_MANAGER_NAME
    );
    expect(receiptManagerData.parsed.paymentManager.toString()).toEqual(
      payamentManagerId.toString()
    );
    expect(receiptManagerData.parsed.authority.toString()).toEqual(
      provider.wallet.publicKey.toString()
    );
    expect(receiptManagerData.parsed.paymentMint.toString()).toEqual(
      paymentMint.toString()
    );
    expect(receiptManagerData.parsed.stakePool.toString()).toEqual(
      stakePoolId.toString()
    );
    expect(receiptManagerData.parsed.requiredStakeSeconds.toString()).toEqual(
      requiredStakeSeconds.toString()
    );
    expect(receiptManagerData.parsed.stakeSecondsToUse.toString()).toEqual(
      updatedStakeSecondsToUse.toString()
    );
    expect(receiptManagerData.parsed.requiresAuthorization.toString()).toEqual(
      requiresAuthorization.toString()
    );
  });

  it("Close reward receipt manager", async () => {
    const receiptManagerId = findReceiptManagerId(
      stakePoolId,
      receiptManagerName
    );
    const transaction = await withCloseReceiptManager(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        receiptManagerId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const receiptManagerData = await tryGetAccount(() =>
      getReceiptManager(provider.connection, receiptManagerId)
    );
    expect(receiptManagerData).toEqual(null);
  });
});


