src/ExpoMobileWalletAdapterModule.ts
====================================

Last edited: 2023-03-28 15:16:55

Contents:

.. code-block:: ts

    import { requireNativeModule } from 'expo-modules-core';

// It loads the native module object from the JSI or falls back to
// the bridge module (from NativeModulesProxy) if the remote debugger is on.
export default requireNativeModule('ExpoMobileWalletAdapter');


