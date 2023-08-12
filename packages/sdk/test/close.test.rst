packages/sdk/test/close.test.ts
===============================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: ts

    import { Keypair, PublicKey } from '@solana/web3.js';
import spok from 'spok';
import test from 'tape';
import { InitializeArgs, MigrationState, UnlockMethod } from '../src/generated';
import { amman, InitTransactions, killStuckProcess } from './setup';
import { findMigrationState } from './utils/pdas';

killStuckProcess();

test('Close: successfully close migration state account', async (t) => {
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

  const { tx: closeTx } = await API.close(handler, payer, migrationState);
  await closeTx.assertSuccess(t);

  // const account = await connection.getAccountInfo(migrationState);
  // t.equal(account, null, 'account is null');
});

test('Close: cannot close another migration state account', async (t) => {
  const API = new InitTransactions();
  const { fstTxHandler: handler, payerPair: payer, connection } = await API.payer();

  const defaultKey = new PublicKey('11111111111111111111111111111111');

  const newAuthority = new Keypair();
  await amman.airdrop(connection, newAuthority.publicKey, 1);

  const { tx: tx1, mint } = await API.mintNft(handler, connection, newAuthority, newAuthority);
  await tx1.assertSuccess(t);

  const args: InitializeArgs = {
    ruleSet: defaultKey,
    unlockMethod: UnlockMethod.Timed,
    collectionSize: 0,
  };

  const { tx: transaction, migrationState } = await API.initialize(
    handler,
    newAuthority,
    newAuthority,
    mint,
    args,
  );
  await transaction.assertSuccess(t);

  const state = await MigrationState.fromAccountAddress(connection, migrationState);
  spok(t, state.collectionInfo, {
    authority: newAuthority.publicKey,
    mint: mint,
    ruleSet: defaultKey,
    delegateRecord: defaultKey,
    size: 0,
  });
  spok(t, state.status, {
    inProgress: false,
    isLocked: true,
  });

  const { tx: closeTx } = await API.close(handler, payer, migrationState);
  await closeTx.assertError(t, /Authority does not match the authority on the account/);

  const account = await connection.getAccountInfo(migrationState);
  t.equal(account != null, true);
});

test('Close: empty migration state account fails', async (t) => {
  const API = new InitTransactions();
  const { fstTxHandler: handler, payerPair: payer, connection } = await API.payer();

  const defaultKey = new PublicKey('11111111111111111111111111111111');

  const newAuthority = new Keypair();
  await amman.airdrop(connection, newAuthority.publicKey, 1);

  const { tx: tx1, mint } = await API.mintNft(handler, connection, newAuthority, newAuthority);
  await tx1.assertSuccess(t);

  const args: InitializeArgs = {
    ruleSet: defaultKey,
    unlockMethod: UnlockMethod.Timed,
    collectionSize: 0,
  };

  const { tx: transaction, migrationState } = await API.initialize(
    handler,
    newAuthority,
    newAuthority,
    mint,
    args,
  );
  await transaction.assertSuccess(t);

  const fakeMint = new Keypair().publicKey;
  const emptyMigrationState = findMigrationState(fakeMint);

  const { tx: closeTx } = await API.close(handler, payer, emptyMigrationState);
  await closeTx.assertError(t, /Incorrect program owner for migration state account/);

  const account = await connection.getAccountInfo(migrationState);
  t.equal(account != null, true);
});


