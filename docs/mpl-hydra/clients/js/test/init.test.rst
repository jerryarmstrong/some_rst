clients/js/test/init.test.ts
============================

Last edited: 2023-06-19 18:36:17

Contents:

.. code-block:: ts

    import {
  generateRandomString,
  none,
  publicKey,
} from '@metaplex-foundation/umi';
import test from 'ava';
import {
  Fanout,
  fetchFanout,
  findFanoutNativeAccountPda,
  findFanoutPda,
  init,
  MembershipModel,
} from '../src';
import { createUmi } from './_setup';

test('it can create a fanout account', async (t) => {
  // Given a name.
  const umi = await createUmi();
  const name = generateRandomString();

  // When we create a new fanout account from it.
  await init(umi, {
    name,
    model: MembershipModel.Wallet,
    totalShares: 100,
  }).sendAndConfirm(umi);

  // Then a new fanout account was created with the right data.
  const [fanout, fanoutBump] = findFanoutPda(umi, { name });
  const nativeAccount = findFanoutNativeAccountPda(umi, { fanout });
  const fanoutAccount = await fetchFanout(umi, fanout);
  t.like(fanoutAccount, <Fanout>{
    publicKey: publicKey(fanout),
    authority: publicKey(umi.identity),
    name,
    accountKey: publicKey(nativeAccount),
    totalShares: 100n,
    totalMembers: 0n,
    totalInflow: 0n,
    lastSnapshotAmount: 0n,
    bumpSeed: fanoutBump,
    totalAvailableShares: 100n,
    membershipModel: MembershipModel.Wallet,
    membershipMint: none(),
    totalStakedShares: none(),
  });
});


