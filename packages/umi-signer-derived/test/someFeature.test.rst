packages/umi-signer-derived/test/someFeature.test.ts
====================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import test from 'ava';
import { createDerivedSigner } from '../src';

test('example test', async (t) => {
  t.is(typeof createDerivedSigner, 'function');
});


