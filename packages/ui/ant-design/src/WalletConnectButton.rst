packages/ui/ant-design/src/WalletConnectButton.tsx
==================================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: tsx

    import type { ButtonProps } from 'antd';
import React from 'react';
import { BaseWalletConnectButton } from './BaseWalletConnectButton.js';

const LABELS = {
    connecting: 'Connecting ...',
    connected: 'Connected',
    'has-wallet': 'Connect',
    'no-wallet': 'Connect Wallet',
} as const;

export function WalletConnectButton(props: ButtonProps) {
    return <BaseWalletConnectButton {...props} labels={LABELS} />;
}


