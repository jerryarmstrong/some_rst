app/tx/[signature]/page.tsx
===========================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { SignatureProps } from '@utils/index';
import { Metadata } from 'next/types';
import React from 'react';

import TransactionDetailsPageClient from './page-client';

type Props = Readonly<{
    params: SignatureProps;
}>;

export async function generateMetadata({ params: { signature } }: Props): Promise<Metadata> {
    return {
        description: `Details of the Solana transaction with signature ${signature}`,
        title: `Transaction | ${signature} | Solana`,
    };
}

export default function TransactionDetailsPage(props: Props) {
    return <TransactionDetailsPageClient {...props} />;
}


