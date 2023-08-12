packages/ui/material-ui/src/BaseWalletConnectionButton.tsx
==========================================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: tsx

    import type { ButtonProps } from '@mui/material';
import { Button } from '@mui/material';
import type { WalletName } from '@solana/wallet-adapter-base';
import React from 'react';
import { WalletIcon } from './WalletIcon.js';

type Props = ButtonProps & {
    walletIcon?: string;
    walletName?: WalletName;
};

export const BaseWalletConnectionButton = React.forwardRef(function BaseWalletConnectionButton(
    { color = 'primary', type = 'button', walletIcon, walletName, variant = 'contained', ...props }: Props,
    forwardedRef: React.Ref<HTMLButtonElement>
) {
    return (
        <Button
            {...props}
            color={color}
            startIcon={
                walletIcon && walletName ? (
                    <WalletIcon wallet={{ adapter: { icon: walletIcon, name: walletName } }} />
                ) : undefined
            }
            ref={forwardedRef}
            type={type}
            variant={variant}
        />
    );
});


