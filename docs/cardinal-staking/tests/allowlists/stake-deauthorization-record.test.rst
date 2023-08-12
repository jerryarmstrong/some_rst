tests/allowlists/stake-deauthorization-record.test.ts
=====================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { tryGetAccount } from "@cardinal/common";
import type { PublicKey } from "@solana/web3.js";
import { Transaction } from "@solana/web3.js";

import {
  authorizeStakeEntry,
  createStakeEntry,
  createStakePool,
} from "../../src";
import {
  getStakeAuthorization,
  getStakeAuthorizationsForPool,
  getStakePool,
} from "../../src/programs/stakePool/accounts";
import { findStakeAuthorizationId } from "../../src/programs/stakePool/pda";
import { withDeauthorizeStakeEntry } from "../../src/programs/stakePool/transaction";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Requires authorization success", () => {
  let provider: CardinalProvider;
  const overlayText = "staking";
  let originalMintId: PublicKey;
  let stakePoolId: PublicKey;

  beforeAll(async () => {
    provider = await getProvider();
    // original mint
    [, originalMintId] = await createMasterEdition(
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

  it("Deathorize mint for stake", async () => {
    const transaction = await withDeauthorizeStakeEntry(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeAuthorizationData = await tryGetAccount(async () =>
      getStakeAuthorization(
        provider.connection,
        findStakeAuthorizationId(stakePoolId, originalMintId)
      )
    );
    expect(stakeAuthorizationData).toEqual(null);

    const stakeAuthorizationsForPool = await getStakeAuthorizationsForPool(
      provider.connection,
      stakePoolId
    );
    expect(stakeAuthorizationsForPool.length).toEqual(0);
  });

  it("Init stake entry for pool", async () => {
    let transaction: Transaction;

    [transaction, stakePoolId] = await createStakeEntry(
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        originalMintId: originalMintId,
      }
    );
    await expect(
      executeTransaction(provider.connection, transaction, provider.wallet, {
        silent: true,
      })
    ).rejects.toThrow();
  });
});


