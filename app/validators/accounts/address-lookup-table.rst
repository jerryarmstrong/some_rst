app/validators/accounts/address-lookup-table.ts
===============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: ts

    /* eslint-disable @typescript-eslint/no-redeclare */

import { BigIntFromString, NumberFromString } from '@validators/number';
import { PublicKeyFromString } from '@validators/pubkey';
import { array, enums, Infer, number, optional, type } from 'superstruct';

export type AddressLookupTableAccountType = Infer<typeof AddressLookupTableAccountType>;
export const AddressLookupTableAccountType = enums(['uninitialized', 'lookupTable']);

export type AddressLookupTableAccountInfo = Infer<typeof AddressLookupTableAccountInfo>;
export const AddressLookupTableAccountInfo = type({
    addresses: array(PublicKeyFromString),
    authority: optional(PublicKeyFromString),
    deactivationSlot: BigIntFromString,
    lastExtendedSlot: NumberFromString,
    lastExtendedSlotStartIndex: number(),
});

export type ParsedAddressLookupTableAccount = Infer<typeof ParsedAddressLookupTableAccount>;
export const ParsedAddressLookupTableAccount = type({
    info: AddressLookupTableAccountInfo,
    type: AddressLookupTableAccountType,
});


