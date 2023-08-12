src/ExpoMobileWalletAdapterView.tsx
===================================

Last edited: 2023-03-28 15:16:55

Contents:

.. code-block:: tsx

    import { requireNativeViewManager } from 'expo-modules-core';
import * as React from 'react';

import { ExpoMobileWalletAdapterViewProps } from './ExpoMobileWalletAdapter.types';

const NativeView: React.ComponentType<ExpoMobileWalletAdapterViewProps> =
  requireNativeViewManager('ExpoMobileWalletAdapter');

export default function ExpoMobileWalletAdapterView(props: ExpoMobileWalletAdapterViewProps) {
  return <NativeView {...props} />;
}


