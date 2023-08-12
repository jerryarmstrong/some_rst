packages/transactions/src/accounts.ts
=====================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress, getBase58EncodedAddressComparator } from '@solana/addresses';
import {
    AccountRole,
    IAccountLookupMeta,
    IAccountMeta,
    IInstruction,
    isSignerRole,
    isWritableRole,
    mergeRoles,
    ReadonlyAccount,
    ReadonlyAccountLookup,
    ReadonlySignerAccount,
    WritableAccount,
    WritableAccountLookup,
    WritableSignerAccount,
} from '@solana/instructions';

export const enum AddressMapEntryType {
    FEE_PAYER,
    LOOKUP_TABLE,
    STATIC,
}

type AddressMap = {
    [address: string]: FeePayerAccountEntry | LookupTableAccountEntry | StaticAccountEntry;
};
type FeePayerAccountEntry = Omit<WritableSignerAccount, 'address'> & {
    [TYPE]: AddressMapEntryType.FEE_PAYER;
};
type LookupTableAccountEntry = Omit<ReadonlyAccountLookup | WritableAccountLookup, 'address'> & {
    [TYPE]: AddressMapEntryType.LOOKUP_TABLE;
};
export type OrderedAccounts = (IAccountMeta | IAccountLookupMeta)[] & { readonly __orderedAccounts: unique symbol };
type StaticAccountEntry = Omit<
    ReadonlyAccount | ReadonlySignerAccount | WritableAccount | WritableSignerAccount,
    'address'
> & { [TYPE]: AddressMapEntryType.STATIC };

function upsert(
    addressMap: AddressMap,
    address: Base58EncodedAddress,
    update: (
        entry: FeePayerAccountEntry | LookupTableAccountEntry | StaticAccountEntry | Record<never, never>
    ) => AddressMap[Base58EncodedAddress]
) {
    addressMap[address] = update(addressMap[address] ?? { role: AccountRole.READONLY });
}

const TYPE = Symbol('AddressMapTypeProperty');
export const ADDRESS_MAP_TYPE_PROPERTY: typeof TYPE = TYPE;

export function getAddressMapFromInstructions(
    feePayer: Base58EncodedAddress,
    instructions: readonly IInstruction[]
): AddressMap {
    const addressMap: AddressMap = {
        [feePayer]: { [TYPE]: AddressMapEntryType.FEE_PAYER, role: AccountRole.WRITABLE_SIGNER },
    };
    const addressesOfInvokedPrograms = new Set<Base58EncodedAddress>();
    for (const instruction of instructions) {
        upsert(addressMap, instruction.programAddress, entry => {
            addressesOfInvokedPrograms.add(instruction.programAddress);
            if (TYPE in entry) {
                if (isWritableRole(entry.role)) {
                    switch (entry[TYPE]) {
                        case AddressMapEntryType.FEE_PAYER:
                            // TODO: Coded error.
                            throw new Error(
                                'This transaction includes an address ' +
                                    `(\`${instruction.programAddress}\`) which is both invoked ` +
                                    'and set as the fee payer. Program addresses may not pay fees.'
                            );
                        default:
                            // TODO: Coded error.
                            throw new Error(
                                'This transaction includes an address ' +
                                    `(\`${instruction.programAddress}\`) which is both invoked ` +
                                    'and marked writable. Program addresses may not be writable.'
                            );
                    }
                }
                if (entry[TYPE] === AddressMapEntryType.STATIC) {
                    return entry;
                }
            }
            return { [TYPE]: AddressMapEntryType.STATIC, role: AccountRole.READONLY };
        });
        let addressComparator: ReturnType<typeof getBase58EncodedAddressComparator>;
        if (!instruction.accounts) {
            continue;
        }
        for (const account of instruction.accounts) {
            upsert(addressMap, account.address, entry => {
                const {
                    // eslint-disable-next-line @typescript-eslint/no-unused-vars
                    address: _,
                    ...accountMeta
                } = account;
                if (TYPE in entry) {
                    switch (entry[TYPE]) {
                        case AddressMapEntryType.FEE_PAYER:
                            // The fee payer already has the highest rank -- it is by definition
                            // writable-signer. Return it, no matter how `account` is configured
                            return entry as FeePayerAccountEntry;
                        case AddressMapEntryType.LOOKUP_TABLE: {
                            const nextRole = mergeRoles(entry.role, accountMeta.role);
                            if ('lookupTableAddress' in accountMeta) {
                                const shouldReplaceEntry =
                                    // Consider using the new LOOKUP_TABLE if its address is different...
                                    entry.lookupTableAddress !== accountMeta.lookupTableAddress &&
                                    // ...and sorts before the existing one.
                                    (addressComparator ||= getBase58EncodedAddressComparator())(
                                        accountMeta.lookupTableAddress,
                                        entry.lookupTableAddress
                                    ) < 0;
                                if (shouldReplaceEntry) {
                                    return {
                                        [TYPE]: AddressMapEntryType.LOOKUP_TABLE,
                                        ...accountMeta,
                                        role: nextRole,
                                    } as LookupTableAccountEntry;
                                }
                            } else if (isSignerRole(accountMeta.role)) {
                                // Upgrade this LOOKUP_TABLE entry to a static entry if it must sign.
                                return {
                                    [TYPE]: AddressMapEntryType.STATIC,
                                    role: nextRole,
                                } as StaticAccountEntry;
                            }
                            if (entry.role !== nextRole) {
                                return {
                                    ...entry,
                                    role: nextRole,
                                } as LookupTableAccountEntry;
                            } else {
                                return entry as LookupTableAccountEntry;
                            }
                        }
                        case AddressMapEntryType.STATIC: {
                            const nextRole = mergeRoles(entry.role, accountMeta.role);
                            if (
                                // Check to see if this address represents a program that is invoked
                                // in this transaction.
                                addressesOfInvokedPrograms.has(account.address)
                            ) {
                                if (isWritableRole(accountMeta.role)) {
                                    // TODO: Coded error.
                                    throw new Error(
                                        'This transaction includes an address ' +
                                            `(\`${account.address}\`) which is both invoked and ` +
                                            'marked writable. Program addresses may not be ' +
                                            'writable.'
                                    );
                                }
                                if (entry.role !== nextRole) {
                                    return {
                                        ...entry,
                                        role: nextRole,
                                    } as StaticAccountEntry;
                                } else {
                                    return entry as StaticAccountEntry;
                                }
                            } else if (
                                'lookupTableAddress' in accountMeta &&
                                // Static accounts can be 'upgraded' to lookup table accounts as
                                // long as they are not require to sign the transaction.
                                !isSignerRole(entry.role)
                            ) {
                                return {
                                    ...accountMeta,
                                    [TYPE]: AddressMapEntryType.LOOKUP_TABLE,
                                    role: nextRole,
                                } as LookupTableAccountEntry;
                            } else {
                                if (entry.role !== nextRole) {
                                    // The account's role ranks higher than the current entry's.
                                    return {
                                        ...entry,
                                        role: nextRole,
                                    } as StaticAccountEntry;
                                } else {
                                    return entry as StaticAccountEntry;
                                }
                            }
                        }
                    }
                }
                if ('lookupTableAddress' in accountMeta) {
                    return {
                        ...accountMeta,
                        [TYPE]: AddressMapEntryType.LOOKUP_TABLE,
                    };
                } else {
                    return {
                        ...accountMeta,
                        [TYPE]: AddressMapEntryType.STATIC,
                    };
                }
            });
        }
    }
    return addressMap;
}

export function getOrderedAccountsFromAddressMap(addressMap: AddressMap): OrderedAccounts {
    let addressComparator: ReturnType<typeof getBase58EncodedAddressComparator>;
    const orderedAccounts: (IAccountMeta | IAccountLookupMeta)[] = Object.entries(addressMap)
        .sort(([leftAddress, leftEntry], [rightAddress, rightEntry]) => {
            // STEP 1: Rapid precedence check. Fee payer, then static addresses, then lookups.
            if (leftEntry[TYPE] !== rightEntry[TYPE]) {
                if (leftEntry[TYPE] === AddressMapEntryType.FEE_PAYER) {
                    return -1;
                } else if (rightEntry[TYPE] === AddressMapEntryType.FEE_PAYER) {
                    return 1;
                } else if (leftEntry[TYPE] === AddressMapEntryType.STATIC) {
                    return -1;
                } else if (rightEntry[TYPE] === AddressMapEntryType.STATIC) {
                    return 1;
                }
            }
            // STEP 2: Sort by signer-writability.
            const leftIsSigner = isSignerRole(leftEntry.role);
            if (leftIsSigner !== isSignerRole(rightEntry.role)) {
                return leftIsSigner ? -1 : 1;
            }
            const leftIsWritable = isWritableRole(leftEntry.role);
            if (leftIsWritable !== isWritableRole(rightEntry.role)) {
                return leftIsWritable ? -1 : 1;
            }
            // STEP 3: Sort by address.
            addressComparator ||= getBase58EncodedAddressComparator();
            if (
                leftEntry[TYPE] === AddressMapEntryType.LOOKUP_TABLE &&
                rightEntry[TYPE] === AddressMapEntryType.LOOKUP_TABLE &&
                leftEntry.lookupTableAddress !== rightEntry.lookupTableAddress
            ) {
                return addressComparator(leftEntry.lookupTableAddress, rightEntry.lookupTableAddress);
            } else {
                return addressComparator(leftAddress, rightAddress);
            }
        })
        .map(([address, addressMeta]) => ({
            address: address as Base58EncodedAddress<typeof address>,
            ...addressMeta,
        }));
    return orderedAccounts as unknown as OrderedAccounts;
}


