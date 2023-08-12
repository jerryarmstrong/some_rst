app/block/[slot]/accounts/page.tsx
==================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Metadata } from 'next/types';

import BlockAccountsTabClient from './page-client';

type Props = Readonly<{
    params: {
        slot: string;
    };
}>;

export async function generateMetadata({ params: { slot } }: Props): Promise<Metadata> {
    return {
        description: `Statistics pertaining to accounts which were accessed or written to during block ${slot} on Solana`,
        title: `Accounts Active In Block | ${slot} | Solana`,
    };
}

export default function BlockAccountsTab(props: Props) {
    return <BlockAccountsTabClient {...props} />;
}


