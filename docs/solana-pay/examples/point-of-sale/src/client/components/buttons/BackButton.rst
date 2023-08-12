examples/point-of-sale/src/client/components/buttons/BackButton.tsx
===================================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: tsx

    import React, { FC, HTMLAttributes, ReactNode } from 'react';
import { BackIcon } from '../images/BackIcon';
import css from './BackButton.module.css';

export interface BackButtonProps {
    children: ReactNode;
    onClick: HTMLAttributes<HTMLButtonElement>['onClick'];
}

export const BackButton: FC<BackButtonProps> = ({ children, onClick }) => {
    return (
        <button className={css.button} type="button" onClick={onClick}>
            <BackIcon />
            {children}
        </button>
    );
};


