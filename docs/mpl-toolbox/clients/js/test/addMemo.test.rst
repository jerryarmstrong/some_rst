clients/js/test/addMemo.test.ts
===============================

Last edited: 2023-06-19 17:40:55

Contents:

.. code-block:: ts

    import test from 'ava';
import { addMemo } from '../src';
import { createUmi } from './_setup';

test('it can add a memo to a transaction', async (t) => {
  // Given a context.
  const umi = await createUmi();

  // When we add a memo to a transaction.
  const { signature } = await addMemo(umi, {
    memo: 'Hello world!',
  }).sendAndConfirm(umi);

  // Then the instruction data contains our memo.
  const transaction = await umi.rpc.getTransaction(signature);
  const firstInstructionData =
    transaction?.message.instructions[0].data ?? new Uint8Array();
  const firstInstructionDataString = umi.serializer
    .string()
    .deserialize(firstInstructionData)[0];
  t.is(firstInstructionDataString, 'Hello world!');
});


