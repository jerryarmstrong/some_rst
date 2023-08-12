packages/rpc-core/src/rpc-methods/__tests__/get-token-largest-accounts-test.ts
==============================================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Commitment } from '../common';

describe('getTokenLargestAccounts', () => {
    (['confirmed', 'finalized', 'processed'] as Commitment[]).forEach(commitment => {
        describe(`when called with \`${commitment}\` commitment`, () => {
            // TODO: will need a way to create token mint + accounts in tests
            it.todo('returns the 20 largest token accounts');
        });
    });
});


