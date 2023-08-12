app/block/[slot]/page.tsx
=========================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Metadata } from 'next/types';

import BlockTransactionsTabClient from './page-client';

type Props = Readonly<{
    params: {
        slot: string;
    };
}>;

export async function generateMetadata({ params: { slot } }: Props): Promise<Metadata> {
    return {
        description: `History of all transactions during block ${slot} on Solana`,
        title: `Block | ${slot} | Solana`,
    };
}

export default function BlockTransactionsTab(props: Props) {
    return <BlockTransactionsTabClient {...props} />;
}


