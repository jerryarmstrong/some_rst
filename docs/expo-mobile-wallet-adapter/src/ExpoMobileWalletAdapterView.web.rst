src/ExpoMobileWalletAdapterView.web.tsx
=======================================

Last edited: 2023-03-28 15:16:55

Contents:

.. code-block:: tsx

    import * as React from 'react';

import { ExpoMobileWalletAdapterViewProps } from './ExpoMobileWalletAdapter.types';

export default function ExpoMobileWalletAdapterView(props: ExpoMobileWalletAdapterViewProps) {
  return (
    <div>
      <span>{props.name}</span>
    </div>
  );
}


