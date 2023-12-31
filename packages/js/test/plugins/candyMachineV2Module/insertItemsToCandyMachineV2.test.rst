packages/js/test/plugins/candyMachineV2Module/insertItemsToCandyMachineV2.test.ts
=================================================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import test from 'tape';
import { assertThrows, killStuckProcess, metaplex } from '../../helpers';
import { createCandyMachineV2 } from './helpers';
import {
  MAX_NAME_LENGTH,
  MAX_URI_LENGTH,
} from '@/plugins/candyMachineV2Module/constants';
import { toBigNumber } from '@/index';

killStuckProcess();

test('[candyMachineV2Module] it can add items to a candy machine', async (t) => {
  // Given an existing Candy Machine with a capacity of 100 items.
  const mx = await metaplex();
  const { candyMachine } = await createCandyMachineV2(mx, {
    itemsAvailable: toBigNumber(100),
  });

  // When we add two items to the Candy Machine.
  await mx.candyMachinesV2().insertItems({
    candyMachine,
    authority: mx.identity(),
    items: [
      { name: 'Degen #1', uri: 'https://example.com/degen/1' },
      { name: 'Degen #2', uri: 'https://example.com/degen/2' },
    ],
  });

  const updatedCandyMachine = await mx.candyMachinesV2().refresh(candyMachine);

  // Then the Candy Machine has been updated properly.
  t.false(updatedCandyMachine.isFullyLoaded);
  t.equals(updatedCandyMachine.itemsLoaded.toNumber(), 2);
  t.equals(updatedCandyMachine.items.length, 2);
  t.deepEquals(updatedCandyMachine.items, [
    { name: 'Degen #1', uri: 'https://example.com/degen/1' },
    { name: 'Degen #2', uri: 'https://example.com/degen/2' },
  ]);
});

test('[candyMachineV2Module] it cannot add items that would make the candy machine exceed the maximum capacity', async (t) => {
  // Given an existing Candy Machine with a capacity of 2 items.
  const mx = await metaplex();
  const { candyMachine } = await createCandyMachineV2(mx, {
    itemsAvailable: toBigNumber(2),
  });

  // When we try to add 3 items to the Candy Machine.
  const promise = mx.candyMachinesV2().insertItems({
    candyMachine,
    authority: mx.identity(),
    items: [
      { name: 'Degen #1', uri: 'https://example.com/degen/1' },
      { name: 'Degen #2', uri: 'https://example.com/degen/2' },
      { name: 'Degen #3', uri: 'https://example.com/degen/3' },
    ],
  });

  // Then we expect an error to be thrown.
  await assertThrows(t, promise, /CandyMachineV2CannotAddAmountError/);
});

test('[candyMachineV2Module] it cannot add items once the candy machine is fully loaded', async (t) => {
  // Given an existing Candy Machine with 2 items loaded and a capacity of 2 items.
  const mx = await metaplex();
  const { candyMachine } = await createCandyMachineV2(mx, {
    itemsAvailable: toBigNumber(2),
    items: [
      { name: 'Degen #1', uri: 'https://example.com/degen/1' },
      { name: 'Degen #2', uri: 'https://example.com/degen/2' },
    ],
  });

  // When we try to add one more item to the Candy Machine.
  const promise = mx.candyMachinesV2().insertItems({
    candyMachine,
    authority: mx.identity(),
    items: [{ name: 'Degen #3', uri: 'https://example.com/degen/3' }],
  });

  // Then we expect an error to be thrown.
  await assertThrows(t, promise, /CandyMachineV2IsFullError/);
});

test('[candyMachineV2Module] it cannot add items if either of them have a name or URI that is too long', async (t) => {
  // Given an existing Candy Machine.
  const mx = await metaplex();
  const { candyMachine } = await createCandyMachineV2(mx);

  // When we try to add items that are too long.
  const promise = mx.candyMachinesV2().insertItems({
    candyMachine,
    authority: mx.identity(),
    items: [
      { name: 'Degen #1', uri: 'https://example.com/degen/1' },
      {
        name: 'x'.repeat(MAX_NAME_LENGTH + 1),
        uri: 'https://example.com/degen/2',
      },
      { name: 'Degen #3', uri: 'x'.repeat(MAX_URI_LENGTH + 1) },
    ],
  });

  // Then we expect an error to be thrown.
  await assertThrows(
    t,
    promise,
    /CandyMachineV2AddItemConstraintsViolatedError/
  );
});

test('[candyMachineV2Module] it can add items to a custom offset and override existing items', async (t) => {
  // Given an existing Candy Machine with 2 items loaded and capacity of 3 items.
  const mx = await metaplex();
  const { candyMachine } = await createCandyMachineV2(mx, {
    itemsAvailable: toBigNumber(3),
    items: [
      { name: 'Degen #1', uri: 'https://example.com/degen/1' },
      { name: 'Degen #2', uri: 'https://example.com/degen/2' },
    ],
  });

  // When we add 2 items to the Candy Machine at index 1.
  await mx.candyMachinesV2().insertItems({
    candyMachine,
    authority: mx.identity(),
    index: toBigNumber(1),
    items: [
      { name: 'Degen #3', uri: 'https://example.com/degen/3' },
      { name: 'Degen #4', uri: 'https://example.com/degen/4' },
    ],
  });

  const updatedCandyMachine = await mx.candyMachinesV2().refresh(candyMachine);

  // Then the Candy Machine has been updated properly.
  t.true(updatedCandyMachine.isFullyLoaded);
  t.equals(updatedCandyMachine.itemsLoaded.toNumber(), 3);
  t.equals(updatedCandyMachine.items.length, 3);

  // And the item of index 1 was overriden.
  t.deepEquals(updatedCandyMachine.items, [
    { name: 'Degen #1', uri: 'https://example.com/degen/1' },
    { name: 'Degen #3', uri: 'https://example.com/degen/3' },
    { name: 'Degen #4', uri: 'https://example.com/degen/4' },
  ]);
});


