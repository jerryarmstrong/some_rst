test/someFeature.test.ts
========================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import test from 'ava';
import { createFromIdls } from '../src';

test('example test', async (t) => {
  t.is(typeof createFromIdls, 'function');
});


