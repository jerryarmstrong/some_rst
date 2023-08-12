tests/allowlists/stake-authorization-record.test.ts
===================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { findAta } from "@cardinal/common";
import { getAccount } from "@solana/spl-token";
import type { PublicKey, Transaction } from "@solana/web3.js";

import {
  authorizeStakeEntry,
  createStakeEntry,
  createStakePool,
  stake,
} from "../../src";
import { ReceiptType } from "../../src/programs/stakePool";
import {
  getStakeAuthorization,
  getStakeAuthorizationsForPool,
  getStakeEntry,
  getStakePool,
} from "../../src/programs/stakePool/accounts";
import { findStakeAuthorizationId } from "../../src/programs/stakePool/pda";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Requires authorization success", () => {
  let provider: CardinalProvider;
  const overlayText = "staking";
  let originalMintTokenAccountId: PublicKey;
  let originalMintId: PublicKey;
  let stakePoolId: PublicKey;

  beforeAll(async () => {
    provider = await getProvider();
    // original mint
    [originalMintTokenAccountId, originalMintId] = await createMasterEdition(
      provider.connection,
      provider.wallet
    );
  });

  it("Create Pool", async () => {
    let transaction: Transaction;
    [transaction, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {
        overlayText: overlayText,
        requiresCreators: [],
        requiresAuthorization: true,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakePoolData = await getStakePool(provider.connection, stakePoolId);
    expect(stakePoolData.parsed.overlayText).toEqual(overlayText);
    expect(stakePoolData.parsed.requiresAuthorization).toBeTruthy();
  });

  it("Authorize mint for stake", async () => {
    const transaction = await authorizeStakeEntry(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeAuthorizationData = await getStakeAuthorization(
      provider.connection,
      findStakeAuthorizationId(stakePoolId, originalMintId)
    );

    expect(stakeAuthorizationData).not.toEqual(null);

    const stakeAuthorizationsForPool = await getStakeAuthorizationsForPool(
      provider.connection,
      stakePoolId
    );
    expect(stakeAuthorizationsForPool.length).toEqual(1);
    expect(stakeAuthorizationData.pubkey.toString()).toEqual(
      stakeAuthorizationsForPool[0]?.pubkey.toString()
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


