packages/transactions/src/compile-static-accounts.ts
====================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';

import { OrderedAccounts } from './accounts';

export function getCompiledStaticAccounts(orderedAccounts: OrderedAccounts): Base58EncodedAddress[] {
    const firstLookupTableAccountIndex = orderedAccounts.findIndex(account => 'lookupTableAddress' in account);
    const orderedStaticAccounts =
        firstLookupTableAccountIndex === -1 ? orderedAccounts : orderedAccounts.slice(0, firstLookupTableAccountIndex);
    return orderedStaticAccounts.map(({ address }) => address);
}


