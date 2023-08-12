clients/js/test/closeLut.test.ts
================================

Last edited: 2023-06-19 17:40:55

Contents:

.. code-block:: ts

    import { generateSigner, transactionBuilder } from '@metaplex-foundation/umi';
import test from 'ava';
import {
  closeLut,
  createEmptyLut,
  deactivateLut,
  findAddressLookupTablePda,
} from '../src';
import { createUmi } from './_setup';

test('it cannot close a LUT that is not deactivated', async (t) => {
  // Given an existing LUT that is not deactivated.
  const umi = await createUmi();
  const recentSlot = await umi.rpc.getSlot({ commitment: 'finalized' });
  const lut = findAddressLookupTablePda(umi, {
    authority: umi.identity.publicKey,
    recentSlot,
  });
  await createEmptyLut(umi, { recentSlot }).sendAndConfirm(umi);

  // When we try to close it.
  const recipient = generateSigner(umi).publicKey;
  const promise = closeLut(umi, {
    address: lut,
    recipient,
  }).sendAndConfirm(umi);

  // Then we expect a program error.
  const error: any = await t.throwsAsync(promise);
  const message = 'Lookup table is not deactivated';
  t.true(error.logs.join('').includes(message));
});

test('it cannot close a LUT that has just been deactivated', async (t) => {
  // Given a LUT that has just been deactivated.
  const umi = await createUmi();
  const recentSlot = await umi.rpc.getSlot({ commitment: 'finalized' });
  const lut = findAddressLookupTablePda(umi, {
    authority: umi.identity.publicKey,
    recentSlot,
  });
  await transactionBuilder()
    .add(createEmptyLut(umi, { recentSlot }))
    .add(deactivateLut(umi, { address: lut }))
    .sendAndConfirm(umi);

  // When we try to close it.
  const recipient = generateSigner(umi).publicKey;
  const promise = closeLut(umi, {
    address: lut,
    recipient,
  }).sendAndConfirm(umi);

  // Then we expect a program error.
  const error: any = await t.throwsAsync(promise);
  const message =
    /Table cannot be closed until it's fully deactivated in \d+ blocks/;
  t.true(message.test(error.logs.join('')));
});


