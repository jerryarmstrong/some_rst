app/address/[address]/security/page.tsx
=======================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import getReadableTitleFromAddress, { AddressPageMetadataProps } from '@utils/get-readable-title-from-address';
import { Metadata } from 'next/types';

import SecurityPageClient from './page-client';

export async function generateMetadata(props: AddressPageMetadataProps): Promise<Metadata> {
    return {
        description: `Contents of the security.txt for the program with address ${props.params.address} on Solana`,
        title: `Security | ${await getReadableTitleFromAddress(props)} | Solana`,
    };
}

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

export default function SecurityPage(props: Props) {
    return <SecurityPageClient {...props} />;
}


