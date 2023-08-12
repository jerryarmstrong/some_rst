src/index.tsx
=============

Last edited: 2023-03-27 15:10:41

Contents:

.. code-block:: tsx

    import { NativeModules, Platform } from 'react-native';

const LINKING_ERROR =
  `The package 'mobile-wallet-adapter' doesn't seem to be linked. Make sure: \n\n` +
  Platform.select({ ios: "- You have run 'pod install'\n", default: '' }) +
  '- You rebuilt the app after installing the package\n' +
  '- You are not using Expo Go\n';

const MobileWalletAdapterLibrary = NativeModules.MobileWalletAdapterLibrary
  ? NativeModules.MobileWalletAdapterLibrary
  : new Proxy(
      {},
      {
        get() {
          throw new Error(LINKING_ERROR);
        },
      }
    );

export function multiply(a: number, b: number): Promise<number> {
  return MobileWalletAdapterLibrary.multiply(a, b);
}


