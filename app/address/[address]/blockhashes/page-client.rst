app/address/[address]/blockhashes/page-client.tsx
=================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    'use client';

import { BlockhashesCard } from '@components/account/BlockhashesCard';
import { ParsedAccountRenderer } from '@components/account/ParsedAccountRenderer';
import React from 'react';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

function BlockhashesCardRenderer({
    account,
    onNotFound,
}: React.ComponentProps<React.ComponentProps<typeof ParsedAccountRenderer>['renderComponent']>) {
    const parsedData = account?.data?.parsed;
    if (!parsedData || parsedData.program !== 'sysvar' || parsedData.parsed.type !== 'recentBlockhashes') {
        return onNotFound();
    }
    return <BlockhashesCard blockhashes={parsedData.parsed.info} />;
}

export default function RecentBlockhashesPageClient({ params: { address } }: Props) {
    return <ParsedAccountRenderer address={address} renderComponent={BlockhashesCardRenderer} />;
}


