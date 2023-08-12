tests/allowlists/stake-authorization-record-fail.test.ts
========================================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { PublicKey, Transaction } from "@solana/web3.js";

import { createStakeEntry, createStakePool } from "../../src";
import { getStakePool } from "../../src/programs/stakePool/accounts";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Requires authorization fail", () => {
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
        requiresAuthorization: true,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakePoolData = await getStakePool(provider.connection, stakePoolId);
    expect(stakePoolData.parsed.requiresAuthorization).toBeTruthy();
    expect(stakePoolData.parsed.overlayText).toEqual(overlayText);
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


