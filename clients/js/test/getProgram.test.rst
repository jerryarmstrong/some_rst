clients/js/test/getProgram.test.ts
==================================

Last edited: 2023-08-12 00:00:44

Contents:

.. code-block:: ts

    import { samePublicKey } from '@metaplex-foundation/umi';
import test from 'ava';
import { MPL_BUBBLEGUM_PROGRAM_ID } from '../src';
import { createUmi } from './_setup';

test('it registers the program', async (t) => {
  // Given a Umi instance using the project's plugin.
  const umi = await createUmi();

  // When we fetch the registered program.
  const program = umi.programs.get('mplBubblegum');

  // Then we expect it to be the same as the program ID constant.
  t.true(samePublicKey(program.publicKey, MPL_BUBBLEGUM_PROGRAM_ID));
});


