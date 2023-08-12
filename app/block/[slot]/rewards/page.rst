app/block/[slot]/rewards/page.tsx
=================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Metadata } from 'next/types';

import BlockRewardsTabClient from './page-client';

type Props = Readonly<{
    params: {
        slot: string;
    };
}>;

export async function generateMetadata({ params: { slot } }: Props): Promise<Metadata> {
    return {
        description: `List of addresses to which rewards were disbursed during block ${slot} on Solana`,
        title: `Block Rewards | ${slot} | Solana`,
    };
}

export default function BlockRewardsTab(props: Props) {
    return <BlockRewardsTabClient {...props} />;
}


