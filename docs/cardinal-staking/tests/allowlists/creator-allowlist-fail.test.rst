tests/allowlists/creator-allowlist-fail.test.ts
===============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { PublicKey, Transaction } from "@solana/web3.js";
import { Keypair } from "@solana/web3.js";

import { createStakeEntry, createStakePool } from "../../src";
import { getStakePool } from "../../src/programs/stakePool/accounts";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Creator allowlist fail", () => {
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
    const creator = Keypair.generate();

    let transaction: Transaction;
    [transaction, stakePoolId] = await createStakePool(
      provider.connection,
      provider.wallet,
      {
        overlayText: overlayText,
        requiresCreators: [creator.publicKey],
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakePoolData = await getStakePool(provider.connection, stakePoolId);
    expect(stakePoolData.parsed.requiresCreators[0]?.toString()).toEqual(
      creator.publicKey.toString()
    );
  });

  it("Init stake entry for pool", async () => {
    const [transaction] = await createStakeEntry(
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


