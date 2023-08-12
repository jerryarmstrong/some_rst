packages/transactions/src/__tests__/compile-header-test.ts
==========================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';
import { AccountRole } from '@solana/instructions';

import { OrderedAccounts } from '../accounts';
import { getCompiledMessageHeader } from '../compile-header';

let _nextMockAddress = 0;
function getMockAddress() {
    return `${_nextMockAddress++}` as Base58EncodedAddress;
}

describe('getCompiledMessageHeader', () => {
    it('counts the number of signers', () => {
        expect(
            getCompiledMessageHeader([
                { address: getMockAddress(), role: AccountRole.WRITABLE_SIGNER },
                { address: getMockAddress(), role: AccountRole.READONLY_SIGNER },
                { address: getMockAddress(), role: AccountRole.READONLY_SIGNER },
                { address: getMockAddress(), role: AccountRole.WRITABLE },
                { address: getMockAddress(), role: AccountRole.READONLY },
                {
                    address: getMockAddress(),
                    addressIndex: 0,
                    lookupTableAddress: getMockAddress(),
                    role: AccountRole.WRITABLE,
                },
                {
                    address: getMockAddress(),
                    addressIndex: 1,
                    lookupTableAddress: getMockAddress(),
                    role: AccountRole.READONLY,
                },
            ] as OrderedAccounts)
        ).toHaveProperty('numSignerAccounts', 3);
    });
    it('counts the number of readonly signers', () => {
        expect(
            getCompiledMessageHeader([
                { address: getMockAddress(), role: AccountRole.WRITABLE_SIGNER },
                { address: getMockAddress(), role: AccountRole.READONLY_SIGNER },
                { address: getMockAddress(), role: AccountRole.READONLY_SIGNER },
                { address: getMockAddress(), role: AccountRole.WRITABLE },
                { address: getMockAddress(), role: AccountRole.READONLY },
                {
                    address: getMockAddress(),
                    addressIndex: 0,
                    lookupTableAddress: getMockAddress(),
                    role: AccountRole.WRITABLE,
                },
                {
                    address: getMockAddress(),
                    addressIndex: 1,
                    lookupTableAddress: getMockAddress(),
                    role: AccountRole.READONLY,
                },
            ] as OrderedAccounts)
        ).toHaveProperty('numReadonlySignerAccounts', 2);
    });
    it('counts the number of readonly non-signers, ignoring lookup table addresses', () => {
        expect(
            getCompiledMessageHeader([
                { address: getMockAddress(), role: AccountRole.WRITABLE_SIGNER },
                { address: getMockAddress(), role: AccountRole.READONLY_SIGNER },
                { address: getMockAddress(), role: AccountRole.READONLY_SIGNER },
                { address: getMockAddress(), role: AccountRole.WRITABLE },
                { address: getMockAddress(), role: AccountRole.READONLY },
                {
                    address: getMockAddress(),
                    addressIndex: 0,
                    lookupTableAddress: getMockAddress(),
                    role: AccountRole.WRITABLE,
                },
                {
                    address: getMockAddress(),
                    addressIndex: 1,
                    lookupTableAddress: getMockAddress(),
                    role: AccountRole.READONLY,
                },
            ] as OrderedAccounts)
        ).toHaveProperty('numReadonlyNonSignerAccounts', 1);
    });
});


