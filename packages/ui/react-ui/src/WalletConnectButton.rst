packages/ui/react-ui/src/WalletConnectButton.tsx
================================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: tsx

    import React from 'react';
import { BaseWalletConnectButton } from './BaseWalletConnectButton.js';
import type { ButtonProps } from './Button.js';

const LABELS = {
    connecting: 'Connecting ...',
    connected: 'Connected',
    'has-wallet': 'Connect',
    'no-wallet': 'Connect Wallet',
} as const;

export function WalletConnectButton(props: ButtonProps) {
    return <BaseWalletConnectButton {...props} labels={LABELS} />;
}


