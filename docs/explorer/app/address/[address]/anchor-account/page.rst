app/address/[address]/anchor-account/page.tsx
=============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import getReadableTitleFromAddress, { AddressPageMetadataProps } from '@utils/get-readable-title-from-address';
import { Metadata } from 'next/types';

import AnchorAccountPageClient from './page-client';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

export async function generateMetadata(props: AddressPageMetadataProps): Promise<Metadata> {
    return {
        description: `Contents of the Anchor Account at address ${props.params.address} on Solana`,
        title: `Anchor Account Data | ${await getReadableTitleFromAddress(props)} | Solana`,
    };
}

export default function AnchorAccountPage(props: Props) {
    return <AnchorAccountPageClient {...props} />;
}


