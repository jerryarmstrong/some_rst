examples/point-of-sale/src/client/components/sections/PoweredBy.tsx
===================================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: tsx

    import React, { FC } from 'react';
import { SolanaPayLogo } from '../images/SolanaPayLogo';
import css from './PoweredBy.module.css';

export const PoweredBy: FC = () => {
    return (
        <div className={css.root}>
            Powered by <SolanaPayLogo />
        </div>
    );
};


