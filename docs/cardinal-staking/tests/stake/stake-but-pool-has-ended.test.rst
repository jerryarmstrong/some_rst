tests/stake/stake-but-pool-has-ended.test.ts
============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import type { PublicKey, Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import { createStakePool, stake } from "../../src";
import { createMasterEdition, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

let provider: CardinalProvider;
let originalMintTokenAccountId: PublicKey;
let originalMintId: PublicKey;
let stakePoolId: PublicKey;
const endDate = Date.now() / 1000 + 2;

describe("Stake pool ended", () => {
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
      { endDate: new BN(endDate) }
    );

    await executeTransaction(provider.connection, tx, provider.wallet);
  });

  it("Stake", async () => {
    await new Promise((r) => setTimeout(r, 3000));
    const tx = await stake(provider.connection, provider.wallet, {
      stakePoolId: stakePoolId,
      originalMintId: originalMintId,
      userOriginalMintTokenAccountId: originalMintTokenAccountId,
    });
    await expect(
      executeTransaction(provider.connection, tx, provider.wallet, {
        silent: true,
      })
    ).rejects.toThrow();
  });
});


