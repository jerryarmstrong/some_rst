tests/stake-receipts/stake-receipts.test.ts
===========================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findAta } from "@cardinal/common";
import { getAccount, getAssociatedTokenAddressSync } from "@solana/spl-token";
import { Keypair, PublicKey, Transaction } from "@solana/web3.js";

import { createStakeEntryAndStakeMint, stake, unstake } from "../../src";
import { ReceiptType } from "../../src/programs/stakePool";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { withInitStakePool } from "../../src/programs/stakePool/transaction";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEditionTx, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

let provider: CardinalProvider;
let originalMintTokenAccountId: PublicKey;
let originalMintId: PublicKey;
let stakePoolId: PublicKey;

beforeAll(async () => {
  provider = await getProvider();

  const mintKeypair = Keypair.generate();
  originalMintId = mintKeypair.publicKey;
  originalMintTokenAccountId = getAssociatedTokenAddressSync(
    originalMintId,
    provider.wallet.publicKey
  );
  await executeTransaction(
    provider.connection,
    await createMasterEditionTx(
      provider.connection,
      mintKeypair.publicKey,
      provider.wallet.publicKey
    ),
    provider.wallet,
    { signers: [mintKeypair] }
  );
});

it("Create Pool", async () => {
  const transaction = new Transaction();

  [, stakePoolId] = await withInitStakePool(
    transaction,
    provider.connection,
    provider.wallet,
    {}
  );
  await executeTransaction(provider.connection, transaction, provider.wallet);
});

it("Init stake entry and mint", async () => {
  const [transaction, , stakeMintKeypair] = await createStakeEntryAndStakeMint(
    provider.connection,
    provider.wallet,
    {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
    }
  );
  await executeTransaction(provider.connection, transaction, provider.wallet, {
    signers: stakeMintKeypair ? [stakeMintKeypair] : [],
  });

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
  expect(stakeEntryData.parsed.pool.toString()).toEqual(stakePoolId.toString());
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

  const userOriginalMintTokenAccountId = await findAta(
    originalMintId,
    provider.wallet.publicKey,
    true
  );

  if (!stakeEntryData.parsed.stakeMint) {
    throw new Error("Receipt mint keypair is null");
  }

  const stakeEntryOriginalMintTokenAccountId = await findAta(
    originalMintId,
    stakeEntryData.pubkey,
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
  expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(0);

  const checkStakeEntryOriginalMintTokenAccount = await getAccount(
    provider.connection,
    stakeEntryOriginalMintTokenAccountId
  );
  expect(Number(checkStakeEntryOriginalMintTokenAccount.amount)).toEqual(1);
});

it("Unstake", async () => {
  const transaction = await unstake(provider.connection, provider.wallet, {
    stakePoolId: stakePoolId,
    originalMintId: originalMintId,
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

  if (!stakeEntryData.parsed.stakeMint) {
    throw new Error("Receipt mint keypair is null");
  }

  const userReceiptMintTokenAccountId = await findAta(
    stakeEntryData.parsed.stakeMint,
    provider.wallet.publicKey,
    true
  );

  const stakeEntryOriginalMintTokenAccountId = await findAta(
    originalMintId,
    stakeEntryData.pubkey,
    true
  );

  const stakeEntryReceiptMintTokenAccountId = await findAta(
    stakeEntryData.parsed.stakeMint,
    stakeEntryData.pubkey,
    true
  );

  expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
  expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
    PublicKey.default.toString()
  );

  const checkUserReceiptMintTokenAccount = await getAccount(
    provider.connection,
    userReceiptMintTokenAccountId
  );
  expect(Number(checkUserReceiptMintTokenAccount.amount)).toEqual(0);

  const checkUserOriginalTokenAccount = await getAccount(
    provider.connection,
    userOriginalMintTokenAccountId
  );
  expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(1);

  const checkStakeEntryOriginalMintTokenAccount = await getAccount(
    provider.connection,
    stakeEntryOriginalMintTokenAccountId
  );
  expect(Number(checkStakeEntryOriginalMintTokenAccount.amount)).toEqual(0);

  const checkStakeEntryReceiptMintTokenAccount = await getAccount(
    provider.connection,
    stakeEntryReceiptMintTokenAccountId
  );
  expect(Number(checkStakeEntryReceiptMintTokenAccount.amount)).toEqual(1);
});


