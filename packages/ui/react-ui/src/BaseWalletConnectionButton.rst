packages/ui/react-ui/src/BaseWalletConnectionButton.tsx
=======================================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: tsx

    import type { WalletName } from '@solana/wallet-adapter-base';
import React from 'react';
import { Button } from './Button.js';
import { WalletIcon } from './WalletIcon.js';

type Props = React.ComponentProps<typeof Button> & {
    walletIcon?: string;
    walletName?: WalletName;
};

export function BaseWalletConnectionButton({ walletIcon, walletName, ...props }: Props) {
    return (
        <Button
            {...props}
            className="wallet-adapter-button-trigger"
            startIcon={
                walletIcon && walletName ? (
                    <WalletIcon wallet={{ adapter: { icon: walletIcon, name: walletName } }} />
                ) : undefined
            }
        />
    );
}


