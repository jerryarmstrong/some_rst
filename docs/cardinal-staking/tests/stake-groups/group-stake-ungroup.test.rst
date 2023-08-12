tests/stake-groups/group-stake-ungroup.test.ts
==============================================

Last edited: 2023-06-10 02:13:42

Contents:

.. code-block:: ts

    import { Wallet } from "@coral-xyz/anchor";
import { getAccount, getAssociatedTokenAddressSync } from "@solana/spl-token";
import type { PublicKey } from "@solana/web3.js";
import { Transaction } from "@solana/web3.js";

import {
  createGroupEntry,
  createStakePool,
  initUngrouping,
  stake,
} from "../../src";
import { ReceiptType } from "../../src/programs/stakePool";
import {
  getGroupStakeEntry,
  getStakeEntry,
} from "../../src/programs/stakePool/accounts";
import { withRemoveFromGroupEntry } from "../../src/programs/stakePool/transaction";
import { findStakeEntryIdFromMint } from "../../src/programs/stakePool/utils";
import {
  createMasterEdition,
  executeTransaction,
  newAccountWithLamports,
} from "../utils";
import type { CardinalProvider } from "../workspace";
import { getProvider } from "../workspace";

describe("Group stake ungroup", () => {
  let provider: CardinalProvider;
  let mintId1: PublicKey;
  let mintId2: PublicKey;
  let mintId3: PublicKey;
  let mintId4: PublicKey;
  let mintId5: PublicKey;
  let mintId6: PublicKey;

  let stakePoolId: PublicKey;
  let groupStakeEntryId: PublicKey;

  beforeAll(async () => {
    provider = await getProvider();
    const mintAuthority = await newAccountWithLamports(provider.connection);
    // mint1
    [, mintId1] = await createMasterEdition(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey }
    );
    // mint2
    [, mintId2] = await createMasterEdition(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey }
    );
    // mint3
    [, mintId3] = await createMasterEdition(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey }
    );
    // mint4
    [, mintId4] = await createMasterEdition(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey }
    );
    // mint5
    [, mintId5] = await createMasterEdition(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey }
    );
    // mint6
    [, mintId6] = await createMasterEdition(
      provider.connection,
      new Wallet(mintAuthority),
      { target: provider.wallet.publicKey }
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

  it("Stake all", async () => {
    const mintIds = [mintId1, mintId2, mintId3, mintId4, mintId5, mintId6];
    for (let i = 0; i < mintIds.length; i++) {
      const mintId = mintIds[i]!;
      const userTokenAccountId = getAssociatedTokenAddressSync(
        mintId,
        provider.wallet.publicKey,
        true
      );
      const transaction = await stake(provider.connection, provider.wallet, {
        stakePoolId: stakePoolId,
        originalMintId: mintId,
        userOriginalMintTokenAccountId: userTokenAccountId,
        receiptType: ReceiptType.Original,
      });
      await executeTransaction(
        provider.connection,
        transaction,
        provider.wallet
      );

      const stakeEntryData = await getStakeEntry(
        provider.connection,
        await findStakeEntryIdFromMint(
          provider.connection,
          provider.wallet.publicKey,
          stakePoolId,
          mintId
        )
      );
      expect(stakeEntryData.parsed.lastStakedAt.toNumber()).toBeGreaterThan(0);
      expect(stakeEntryData.parsed.lastStaker.toString()).toEqual(
        provider.wallet.publicKey.toString()
      );

      const userTokenAccount = await getAccount(
        provider.connection,
        userTokenAccountId
      );
      expect(Number(userTokenAccount.amount)).toEqual(1);
      expect(userTokenAccount.isFrozen).toEqual(true);
    }
  });

  it("Create Group Stake Entry", async () => {
    const mindIds = [mintId1, mintId2, mintId3, mintId4, mintId5, mintId6];
    const stakeEntryIds = await Promise.all(
      mindIds.map((mintId) =>
        findStakeEntryIdFromMint(
          provider.connection,
          provider.wallet.publicKey,
          stakePoolId,
          mintId
        )
      )
    );
    const [transaction, groupEntryId] = await createGroupEntry(
      provider.connection,
      provider.wallet,
      {
        stakeEntryIds,
      }
    );
    groupStakeEntryId = groupEntryId;
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const groupStakeEntryData = await getGroupStakeEntry(
      provider.connection,
      groupEntryId
    );

    expect(groupStakeEntryData.parsed.stakeEntries.length).toEqual(
      stakeEntryIds.length
    );

    for (const id of stakeEntryIds) {
      const stakeEntry = await getStakeEntry(provider.connection, id);
      expect(stakeEntry.parsed.grouped).toEqual(true);
    }
  });

  it("Start cooldown period", async () => {
    const [transaction] = await initUngrouping(
      provider.connection,
      provider.wallet,
      {
        groupEntryId: groupStakeEntryId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const groupStakeEntryData = await getGroupStakeEntry(
      provider.connection,
      groupStakeEntryId
    );

    expect(groupStakeEntryData.parsed.groupCooldownStartSeconds).not.toBeNull();
  });

  it("Remove 1 from group", async () => {
    const mintId = mintId1;
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      mintId
    );
    const [transaction] = await withRemoveFromGroupEntry(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        groupEntryId: groupStakeEntryId,
        stakeEntryId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    const groupStakeEntryData = await getGroupStakeEntry(
      provider.connection,
      groupStakeEntryId
    );

    expect(groupStakeEntryData.parsed.stakeEntries.length).toEqual(5);
    const stakeEntry = await getStakeEntry(provider.connection, stakeEntryId);
    expect(stakeEntry.parsed.grouped).toEqual(false);
  });

  it("Remove remaining from group", async () => {
    const mintIds = [mintId2, mintId3, mintId4, mintId5];
    for (let i = 0; i < mintIds.length; i++) {
      const mintId = mintIds[i]!;
      const stakeEntryId = await findStakeEntryIdFromMint(
        provider.connection,
        provider.wallet.publicKey,
        stakePoolId,
        mintId
      );
      const [transaction] = await withRemoveFromGroupEntry(
        new Transaction(),
        provider.connection,
        provider.wallet,
        {
          groupEntryId: groupStakeEntryId,
          stakeEntryId,
        }
      );
      await executeTransaction(
        provider.connection,
        transaction,
        provider.wallet
      );

      const groupStakeEntryData = await getGroupStakeEntry(
        provider.connection,
        groupStakeEntryId
      );

      expect(groupStakeEntryData.parsed.stakeEntries.length).toEqual(
        mintIds.length - i
      );
      const stakeEntry = await getStakeEntry(provider.connection, stakeEntryId);
      expect(stakeEntry.parsed.grouped).toEqual(false);
    }
  });

  it("Remove last from group", async () => {
    const mintId = mintId6;
    const stakeEntryId = await findStakeEntryIdFromMint(
      provider.connection,
      provider.wallet.publicKey,
      stakePoolId,
      mintId
    );
    const [transaction] = await withRemoveFromGroupEntry(
      new Transaction(),
      provider.connection,
      provider.wallet,
      {
        groupEntryId: groupStakeEntryId,
        stakeEntryId,
      }
    );
    await executeTransaction(provider.connection, transaction, provider.wallet);

    await expect(async () => {
      await getGroupStakeEntry(provider.connection, groupStakeEntryId);
    }).rejects.toThrow();

    const stakeEntry = await getStakeEntry(provider.connection, stakeEntryId);
    expect(stakeEntry.parsed.grouped).toEqual(false);
  });
});


