packages/ui/react-ui/src/WalletModalButton.tsx
==============================================

Last edited: 2023-08-07 04:48:35

Contents:

.. code-block:: tsx

    import type { FC, MouseEvent } from 'react';
import React, { useCallback } from 'react';
import type { ButtonProps } from './Button.js';
import { Button as BaseWalletConnectionButton } from './Button.js';
import { useWalletModal } from './useWalletModal.js';

export const WalletModalButton: FC<ButtonProps> = ({ children = 'Select Wallet', onClick, ...props }) => {
    const { visible, setVisible } = useWalletModal();

    const handleClick = useCallback(
        (event: MouseEvent<HTMLButtonElement>) => {
            if (onClick) onClick(event);
            if (!event.defaultPrevented) setVisible(!visible);
        },
        [onClick, setVisible, visible]
    );

    return (
        <BaseWalletConnectionButton {...props} className="wallet-adapter-button-trigger" onClick={handleClick}>
            {children}
        </BaseWalletConnectionButton>
    );
};


