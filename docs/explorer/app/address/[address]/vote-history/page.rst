app/address/[address]/vote-history/page.tsx
===========================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import getReadableTitleFromAddress, { AddressPageMetadataProps } from '@utils/get-readable-title-from-address';
import { Metadata } from 'next/types';

import VoteHistoryPageClient from './page-client';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

export async function generateMetadata(props: AddressPageMetadataProps): Promise<Metadata> {
    return {
        description: `Vote history of the address ${props.params.address} by slot on Solana`,
        title: `Vote History | ${await getReadableTitleFromAddress(props)} | Solana`,
    };
}

export default function VoteHistoryPage(props: Props) {
    return <VoteHistoryPageClient {...props} />;
}


