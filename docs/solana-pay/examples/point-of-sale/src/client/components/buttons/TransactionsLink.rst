examples/point-of-sale/src/client/components/buttons/TransactionsLink.tsx
=========================================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: tsx

    import Link from 'next/link';
import React, { FC } from 'react';
import { useMediaQuery } from 'react-responsive';
import { useLinkWithQuery } from '../../hooks/useLinkWithQuery';
import { ActivityIcon } from '../images/ActivityIcon';
import css from './TransactionsLink.module.css';

export const TransactionsLink: FC = () => {
    const to = useLinkWithQuery('/transactions');
    const phone = useMediaQuery({ query: '(max-width: 767px)' });

    return (
        <Link href={to} passHref>
            <a className={css.link}>
                <ActivityIcon />
                {phone ? null : 'Recent Transactions'}
            </a>
        </Link>
    );
};


