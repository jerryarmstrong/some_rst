packages/ui/ant-design/src/WalletIcon.tsx
=========================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: tsx

    import type { Wallet } from '@solana/wallet-adapter-react';
import type { DetailedHTMLProps, FC, ImgHTMLAttributes } from 'react';
import React from 'react';

export interface WalletIconProps extends DetailedHTMLProps<ImgHTMLAttributes<HTMLImageElement>, HTMLImageElement> {
    wallet: { adapter: Pick<Wallet['adapter'], 'icon' | 'name'> } | null;
}

export const WalletIcon: FC<WalletIconProps> = ({ wallet, ...props }) => {
    return (
        wallet && (
            <img
                src={wallet.adapter.icon}
                alt={`${wallet.adapter.name} icon`}
                className="wallet-adapter-icon"
                {...props}
            />
        )
    );
};


