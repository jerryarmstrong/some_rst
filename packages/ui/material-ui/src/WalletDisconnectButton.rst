packages/ui/material-ui/src/WalletDisconnectButton.tsx
======================================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: tsx

    import type { ButtonProps } from '@mui/material';
import React from 'react';
import { BaseWalletDisconnectButton } from './BaseWalletDisconnectButton.js';

const LABELS = {
    disconnecting: 'Disconnecting ...',
    'has-wallet': 'Disconnect',
    'no-wallet': 'Disconnect Wallet',
} as const;

export function WalletDisconnectButton(props: ButtonProps) {
    return <BaseWalletDisconnectButton {...props} labels={LABELS} />;
}


