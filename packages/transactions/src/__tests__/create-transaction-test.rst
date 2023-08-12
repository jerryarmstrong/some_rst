packages/transactions/src/__tests__/create-transaction-test.ts
==============================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import 'test-matchers/toBeFrozenObject';

import { createTransaction } from '../create-transaction';

describe('createTransaction', () => {
    it('creates a legacy transaction', () => {
        expect(createTransaction({ version: 'legacy' })).toMatchObject({
            instructions: [],
            version: 'legacy',
        });
    });
    it('creates a v0 transaction', () => {
        expect(createTransaction({ version: 0 })).toMatchObject({
            instructions: [],
            version: 0,
        });
    });
    it('freezes the object', () => {
        const tx = createTransaction({ version: 0 });
        expect(tx).toBeFrozenObject();
    });
});


