tests/stake-booster/stake-booster-close.test.ts
===============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { tryGetAccount } from "@cardinal/common";
import { Program } from "@coral-xyz/anchor";
import type { PublicKey } from "@solana/web3.js";
import { Keypair, Transaction } from "@solana/web3.js";
import { BN } from "bn.js";

import { createStakePool } from "../../src";
import type { STAKE_POOL_PROGRAM } from "../../src/programs/stakePool";
import {
  STAKE_POOL_ADDRESS,
  STAKE_POOL_IDL,
} from "../../src/programs/stakePool";
import { getStakeBooster } from "../../src/programs/stakePool/accounts";
import { findStakeBoosterId } from "../../src/programs/stakePool/pda";
import {
  withCloseStakeBooster,
  withInitStakeBooster,
  withUpdateStakeBooster,
} from "../../src/programs/stakePool/transaction";
import { createMint, executeTransaction } from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Stake booster close", () => {
  let provider: CardinalProvider;
  let stakePoolId: PublicKey;
  let paymentMintId: PublicKey;
  const STAKE_BOOSTER_PAYMENT_AMOUNT = new BN(2);
  const BOOST_SECONDS = new BN(10);
  const UPDATE_BOOST_SECONDS = new BN(20);

  beforeAll(async () => {
    provider = await getProvider();
    // payment mint
    [, paymentMintId] = await createMint(provider.connection, provider.wallet, {
      amount: 100,
    });
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

  it("Create booster", async () => {
    const transaction = await withInitStakeBooster(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        paymentAmount: STAKE_BOOSTER_PAYMENT_AMOUNT,
        paymentMint: paymentMintId,
        boostSeconds: BOOST_SECONDS,
        startTimeSeconds: Date.now() / 1000,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeBoosterId = findStakeBoosterId(stakePoolId);
    const stakeBooster = await getStakeBooster(
      provider.connection,
      stakeBoosterId
    );
    expect(stakeBooster.parsed.stakePool.toString()).toEqual(
      stakePoolId.toString()
    );
    expect(stakeBooster.parsed.identifier.toString()).toEqual(
      new BN(0).toString()
    );
    expect(stakeBooster.parsed.boostSeconds.toString()).toEqual(
      BOOST_SECONDS.toString()
    );
    expect(stakeBooster.parsed.paymentAmount.toString()).toEqual(
      STAKE_BOOSTER_PAYMENT_AMOUNT.toString()
    );
    expect(stakeBooster.parsed.paymentMint.toString()).toEqual(
      paymentMintId.toString()
    );
  });

  it("Update booster", async () => {
    const transaction = await withUpdateStakeBooster(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
        paymentAmount: STAKE_BOOSTER_PAYMENT_AMOUNT,
        paymentMint: paymentMintId,
        boostSeconds: UPDATE_BOOST_SECONDS,
        startTimeSeconds: Date.now() / 1000,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeBoosterId = findStakeBoosterId(stakePoolId);
    const stakeBooster = await getStakeBooster(
      provider.connection,
      stakeBoosterId
    );
    expect(stakeBooster.parsed.stakePool.toString()).toEqual(
      stakePoolId.toString()
    );
    expect(stakeBooster.parsed.identifier.toString()).toEqual(
      new BN(0).toString()
    );
    expect(stakeBooster.parsed.boostSeconds.toString()).toEqual(
      UPDATE_BOOST_SECONDS.toString()
    );
    expect(stakeBooster.parsed.paymentAmount.toString()).toEqual(
      STAKE_BOOSTER_PAYMENT_AMOUNT.toString()
    );
    expect(stakeBooster.parsed.paymentMint.toString()).toEqual(
      paymentMintId.toString()
    );
  });

  it("Update booster invalid payment manager", async () => {
    const stakePoolProgram = new Program<STAKE_POOL_PROGRAM>(
      STAKE_POOL_IDL,
      STAKE_POOL_ADDRESS,
      provider
    );
    const stakeBoosterId = findStakeBoosterId(stakePoolId);
    const transaction = new Transaction().add(
      stakePoolProgram.instruction.updateStakeBooster(
        {
          paymentAmount: STAKE_BOOSTER_PAYMENT_AMOUNT,
          paymentMint: paymentMintId,
          boostSeconds: UPDATE_BOOST_SECONDS,
          paymentManager: Keypair.generate().publicKey,
          startTimeSeconds: new BN(Date.now() / 1000),
        },
        {
          accounts: {
            stakePool: stakePoolId,
            stakeBooster: stakeBoosterId,
            authority: provider.wallet.publicKey,
          },
        }
      )
    );
    await expect(
      executeTransaction(provider.connection, transaction, provider.wallet, {
        silent: true,
      })
    ).rejects.toThrow();
  });

  it("Close booster", async () => {
    const stakeBoosterId = findStakeBoosterId(stakePoolId);
    const transaction = await withCloseStakeBooster(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        stakePoolId: stakePoolId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const stakeBooster = await tryGetAccount(() =>
      getStakeBooster(provider.connection, stakeBoosterId)
    );
    expect(stakeBooster).toEqual(null);
  });
});


