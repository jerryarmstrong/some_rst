packages/transactions/src/compile-address-table-lookups.ts
==========================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress, getBase58EncodedAddressComparator } from '@solana/addresses';
import { AccountRole } from '@solana/instructions';

import { OrderedAccounts } from './accounts';

type AddressTableLookup = Readonly<{
    lookupTableAddress: Base58EncodedAddress;
    readableIndices: readonly number[];
    writableIndices: readonly number[];
}>;

export function getCompiledAddressTableLookups(orderedAccounts: OrderedAccounts): AddressTableLookup[] {
    const index: Record<
        Base58EncodedAddress,
        { readonly readableIndices: number[]; readonly writableIndices: number[] }
    > = {};
    for (const account of orderedAccounts) {
        if (!('lookupTableAddress' in account)) {
            continue;
        }
        const entry = (index[account.lookupTableAddress] ||= {
            readableIndices: [],
            writableIndices: [],
        });
        if (account.role === AccountRole.WRITABLE) {
            entry.writableIndices.push(account.addressIndex);
        } else {
            entry.readableIndices.push(account.addressIndex);
        }
    }
    return Object.keys(index)
        .sort(getBase58EncodedAddressComparator())
        .map(lookupTableAddress => ({
            lookupTableAddress: lookupTableAddress as Base58EncodedAddress,
            ...index[lookupTableAddress as unknown as Base58EncodedAddress],
        }));
}


