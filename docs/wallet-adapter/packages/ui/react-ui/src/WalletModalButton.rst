packages/ui/react-ui/src/WalletModalButton.tsx
==============================================

Last edited: 2022-10-02 20:43:04

Contents:

.. code-block:: tsx

    import type { FC, MouseEvent } from 'react';
import React, { useCallback } from 'react';
import type { ButtonProps } from './Button.js';
import { Button } from './Button.js';
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
        <Button className="wallet-adapter-button-trigger" onClick={handleClick} {...props}>
            {children}
        </Button>
    );
};


