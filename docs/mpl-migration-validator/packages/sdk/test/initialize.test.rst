packages/sdk/test/initialize.test.ts
====================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: ts

    import { Keypair, PublicKey, SystemProgram, Transaction } from '@solana/web3.js';
import spok from 'spok';
import test from 'tape';
import {
  createInitializeInstruction,
  InitializeArgs,
  InitializeInstructionAccounts,
  InitializeInstructionArgs,
  MigrationState,
  UnlockMethod,
} from '../src/generated';
import { amman, InitTransactions, killStuckProcess } from './setup';
import { findMetadataAddress, findMigrationState } from './utils/pdas';

killStuckProcess();

test('Initialize: successfully create migration state', async (t) => {
  const API = new InitTransactions();
  const { fstTxHandler: handler, payerPair: payer, connection } = await API.payer();

  const defaultKey = new PublicKey('11111111111111111111111111111111');

  const { tx: tx1, mint } = await API.mintNft(handler, connection, payer, payer);
  await tx1.assertSuccess(t);

  const args: InitializeArgs = {
    ruleSet: defaultKey,
    unlockMethod: UnlockMethod.Timed,
    collectionSize: 0,
  };

  const { tx: transaction, migrationState } = await API.initialize(
    handler,
    payer,
    payer,
    mint,
    args,
  );
  await transaction.assertSuccess(t);

  const state = await MigrationState.fromAccountAddress(connection, migrationState);
  spok(t, state.collectionInfo, {
    authority: payer.publicKey,
    mint: mint,
    ruleSet: defaultKey,
    delegateRecord: defaultKey,
    size: 0,
  });
  spok(t, state.status, {
    inProgress: false,
    isLocked: true,
  });
});

test('Initialize: Cannot initialize twice', async (t) => {
  const API = new InitTransactions();
  const { fstTxHandler: handler, payerPair: payer, connection } = await API.payer();

  const defaultKey = new PublicKey('11111111111111111111111111111111');

  const { tx: tx1, mint } = await API.mintNft(handler, connection, payer, payer);
  await tx1.assertSuccess(t);

  const args: InitializeArgs = {
    ruleSet: defaultKey,
    unlockMethod: UnlockMethod.Timed,
    collectionSize: 0,
  };

  const { tx: transaction, migrationState } = await API.initialize(
    handler,
    payer,
    payer,
    mint,
    args,
  );
  await transaction.assertSuccess(t);

  const state = await MigrationState.fromAccountAddress(connection, migrationState);
  spok(t, state.collectionInfo, {
    authority: payer.publicKey,
    mint: mint,
    ruleSet: defaultKey,
    delegateRecord: defaultKey,
    size: 0,
  });
  spok(t, state.status, {
    inProgress: false,
    isLocked: true,
  });

  const args2: InitializeArgs = {
    ruleSet: defaultKey,
    unlockMethod: UnlockMethod.Vote,
    collectionSize: 0,
  };

  const { tx: transaction2 } = await API.initialize(handler, payer, payer, mint, args2);
  // Our test setup doesn't parse the system program error correctly so
  // we check for logs indicating it fails on the account already being
  // in use.
  await transaction2.assertLogs(t, [/Allocate: account Address/, /already in use/]);
});

test('Initialize: cannot initialize for another authority', async (t) => {
  const API = new InitTransactions();
  const { fstTxHandler: handler, payerPair: payer, connection } = await API.payer();

  const defaultKey = new PublicKey('11111111111111111111111111111111');

  const { tx: tx1, mint } = await API.mintNft(handler, connection, payer, payer);
  await tx1.assertSuccess(t);

  const newAuthority = new Keypair();
  await amman.airdrop(connection, newAuthority.publicKey, 1);

  const args: InitializeArgs = {
    ruleSet: defaultKey,
    unlockMethod: UnlockMethod.Timed,
    collectionSize: 0,
  };

  const collectionMetadata = findMetadataAddress(mint);
  const migrationState = findMigrationState(mint);

  const accounts: InitializeInstructionAccounts = {
    payer: payer.publicKey,
    authority: newAuthority.publicKey,
    collectionMetadata,
    collectionMint: mint,
    migrationState,
    systemProgram: SystemProgram.programId,
  };

  const ixArgs: InitializeInstructionArgs = {
    initializeArgs: args,
  };
  const initializeIx = createInitializeInstruction(accounts, ixArgs);

  const initTx = new Transaction().add(initializeIx);
  const signers = [payer, newAuthority];

  const res = handler.sendAndConfirmTransaction(initTx, signers, 'tx: Initialize');
  await res.assertError(t, /Authority does not match the authority on the account/);
});


