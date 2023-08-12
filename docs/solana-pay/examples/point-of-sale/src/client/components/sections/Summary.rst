examples/point-of-sale/src/client/components/sections/Summary.tsx
=================================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: tsx

    import React, { FC } from 'react';
import { useConfig } from '../../hooks/useConfig';
import { usePayment } from '../../hooks/usePayment';
import { Amount } from './Amount';
import css from './Summary.module.css';

export const Summary: FC = () => {
    const { symbol } = useConfig();
    const { amount } = usePayment();

    return (
        <div className={css.root}>
            <div className={css.title}>Balance Due</div>
            <div className={css.total}>
                <div className={css.totalLeft}>Total</div>
                <div className={css.totalRight}>
                    <div className={css.symbol}>{symbol}</div>
                    <div className={css.amount}>
                        <Amount amount={amount} />
                    </div>
                </div>
            </div>
        </div>
    );
};


