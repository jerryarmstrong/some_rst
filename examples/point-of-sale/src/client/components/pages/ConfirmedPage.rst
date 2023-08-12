examples/point-of-sale/src/client/components/pages/ConfirmedPage.tsx
====================================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: tsx

    import { NextPage } from 'next';
import React from 'react';
import { usePayment } from '../../hooks/usePayment';
import { BackButton } from '../buttons/BackButton';
import { TransactionsLink } from '../buttons/TransactionsLink';
import { PoweredBy } from '../sections/PoweredBy';
import { Progress } from '../sections/Progress';
import css from './ConfirmedPage.module.css';

const ConfirmedPage: NextPage = () => {
    const { reset } = usePayment();

    return (
        <div className={css.root}>
            <div className={css.header}>
                <BackButton onClick={reset}>Start Over</BackButton>
                <TransactionsLink />
            </div>
            <div className={css.main}>
                <Progress />
            </div>
            <div className={css.footer}>
                <PoweredBy />
            </div>
        </div>
    );
};

export default ConfirmedPage;


