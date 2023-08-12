tests/stake/reassign-staker.test.ts
===================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { withFindOrInitAssociatedTokenAccount } from "@cardinal/common";
import { Wallet } from "@coral-xyz/anchor";
import { getAccount, getAssociatedTokenAddressSync } from "@solana/spl-token";
import { Keypair, PublicKey, Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import { createStakePool, stake, unstake } from "../../src";
import { getStakeEntry } from "../../src/programs/stakePool/accounts";
import { findStakeEntryId } from "../../src/programs/stakePool/pda";
import { withReassignStakeEntry } from "../../src/programs/stakePool/transaction";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEditionTx, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider, newAccountWithLamports } from "../workspace";

let provider: CardinalProvider;
let originalMintTokenAccountId: PublicKey;
let originalMintId: PublicKey;
let stakePoolId: PublicKey;
let newStaker: Wallet;

describe("Reassign stake entry", () => {
  beforeAll(async () => {
    provider = await getProvider();

    const mintKeypair = Keypair.generate();
    originalMintId = mintKeypair.publicKey;
    originalMintTokenAccountId = getAssociatedTokenAddressSync(
      originalMintId,
      provider.wallet.publicKey
    );

    newStaker = new Wallet(await newAccountWithLamports(provider.connection));
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
    let tx: Transaction;
    [tx, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {}
    );
    await executeTransaction(provider.connection, tx, provider.wallet);
  });

  it("Stake", async () => {
    const transaction = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      userOriginalMintTokenAccountId: originalMintTokenAccountId,
      amount: new BN(1),
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
    expect(Number(checkUserOriginalTokenAccount.amount)).toEqual(0);
    expect(checkUserOriginalTokenAccount.isFrozen).toEqual(false);
  });

  it("Reassign stake entry", async () => {
    const transaction = new Transaction();
    const stakeEntryId = findStakeEntryId(
      provider.wallet.publicKey,
      stakePoolId,
      originalMintId,
      false
    );
    await withReassignStakeEntry(
      transaction,
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        stakeEntryId: stakeEntryId,
        target: newStaker.publicKey,
      }
    );

    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeEntryData = await getStakeEntry(
      provider.connection,
      stakeEntryId
    );
    expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
      newStaker.publicKey.toString()
    );
  });

  it("Unstake", async () => {
    let transaction = new Transaction();
    await withFindOrInitAssociatedTokenAccount(
      transaction,
      provider.connection,
      originalMintId,
      newStaker.publicKey,
      provider.wallet.publicKey,
      true
    );
    transaction = await unstake(provider.connection, newStaker, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
    });

    await executeTransaction(provider.connection, transaction, newStaker);

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
      newStaker.publicKey,
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


