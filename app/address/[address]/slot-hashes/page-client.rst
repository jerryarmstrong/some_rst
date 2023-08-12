app/address/[address]/slot-hashes/page-client.tsx
=================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    'use client';

import { ParsedAccountRenderer } from '@components/account/ParsedAccountRenderer';
import { SlotHashesCard } from '@components/account/SlotHashesCard';
import React from 'react';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

function SlotHashesCardRenderer({
    account,
    onNotFound,
}: React.ComponentProps<React.ComponentProps<typeof ParsedAccountRenderer>['renderComponent']>) {
    const parsedData = account?.data?.parsed;
    if (!parsedData || parsedData.program !== 'sysvar' || parsedData.parsed.type !== 'slotHashes') {
        return onNotFound();
    }
    return <SlotHashesCard sysvarAccount={parsedData.parsed} />;
}

export default function SlotHashesPageClient({ params: { address } }: Props) {
    return <ParsedAccountRenderer address={address} renderComponent={SlotHashesCardRenderer} />;
}


