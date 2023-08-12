packages/sdk/test/update.test.ts
================================

Last edited: 2023-06-14 20:00:41

Contents:

.. code-block:: ts

    import { Keypair, PublicKey } from '@solana/web3.js';
import spok from 'spok';
import test from 'tape';
import { InitializeArgs, UpdateArgs, MigrationState, UnlockMethod } from '../src/generated';
import { InitTransactions, killStuckProcess } from './setup';

killStuckProcess();

test('Update: successfully update state account', async (t) => {
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
  const newRuleSet = new Keypair().publicKey;

  console.log('newRuleSet', newRuleSet.toBase58());

  const updateArgs: UpdateArgs = {
    ruleSet: newRuleSet,
    collectionSize: null,
  };

  const { tx: updateTx } = await API.update(handler, payer, migrationState, updateArgs);
  await updateTx.assertSuccess(t);

  const newState = await MigrationState.fromAccountAddress(connection, migrationState);
  spok(t, newState.collectionInfo, {
    authority: payer.publicKey,
    mint: mint,
    ruleSet: newRuleSet,
    delegateRecord: defaultKey,
    size: 0,
  });
  spok(t, state.status, {
    inProgress: false,
    isLocked: true,
  });
});

// test.only('Update: Timed method becomes eligible', async (t) => {
//   // This requires updating the contract with a shorter time period to test.
//   const API = new InitTransactions();
//   const { fstTxHandler: handler, payerPair: payer, connection } = await API.payer();

//   const defaultKey = new PublicKey('11111111111111111111111111111111');

//   const { tx: tx1, mint } = await API.mintNft(handler, connection, payer, payer);
//   await tx1.assertSuccess(t);

//   const args: InitializeArgs = {
//     ruleSet: defaultKey,
//     unlockMethod: UnlockMethod.Timed,
//   };

//   const { tx: transaction, migrationState } = await API.initialize(
//     handler,
//     payer,
//     payer,
//     mint,
//     args,
//   );
//   await transaction.assertSuccess(t);

//   const state = await MigrationState.fromAccountAddress(connection, migrationState);
//   spok(t, state, {
//     collectionAuthority: payer.publicKey,
//     collectionMint: mint,
//     ruleSet: defaultKey,
//     collectionDelegate: defaultKey,
//     unlockMethod: args.unlockMethod,
//     migrationSize: 0,
//     inProgress: false,
//     isEligible: false,
//   });

//   await delay(5000);

//   const updateArgs: UpdateArgs = {
//     ruleSet: defaultKey,
//   };

//   const { tx: updateTx } = await API.update(handler, payer, migrationState, updateArgs);
//   await updateTx.assertSuccess(t);

//   const newState = await MigrationState.fromAccountAddress(connection, migrationState);
//   spok(t, newState, {
//     collectionAuthority: payer.publicKey,
//     collectionMint: mint,
//     ruleSet: defaultKey,
//     collectionDelegate: defaultKey,
//     unlockMethod: args.unlockMethod,
//     migrationSize: 0,
//     inProgress: false,
//     isEligible: true,
//   });
// });


