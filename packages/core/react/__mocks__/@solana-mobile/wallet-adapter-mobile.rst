packages/core/react/__mocks__/@solana-mobile/wallet-adapter-mobile.ts
=====================================================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: ts

    import { type WalletName } from '@solana/wallet-adapter-base';
import { MockWalletAdapter } from '../../src/__mocks__/MockWalletAdapter.js';

export const SolanaMobileWalletAdapterWalletName = 'Solana Mobile Wallet Adapter Name For Tests';
export const createDefaultAddressSelector = jest.fn();
export const createDefaultAuthorizationResultCache = jest.fn();
export const createDefaultWalletNotFoundHandler = jest.fn();

class MockSolanaMobileWalletAdapter extends MockWalletAdapter {
    name = SolanaMobileWalletAdapterWalletName as WalletName<string>;
    icon = 'sms.png';
    url = 'https://solanamobile.com';
    publicKey = null;
}

export const SolanaMobileWalletAdapter = jest.fn().mockImplementation(
    (...args) =>
        new MockSolanaMobileWalletAdapter(
            // @ts-ignore
            ...args
        )
);


