app/address/[address]/concurrent-merkle-tree/page-client.tsx
============================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    'use client';

import { ConcurrentMerkleTreeCard } from '@components/account/ConcurrentMerkleTreeCard';
import { ParsedAccountRenderer } from '@components/account/ParsedAccountRenderer';
import { PROGRAM_ID } from '@solana/spl-account-compression';
import React from 'react';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

function ConcurrentMerkleTreeCardRenderer({
    account,
    onNotFound,
}: React.ComponentProps<React.ComponentProps<typeof ParsedAccountRenderer>['renderComponent']>) {
    const rawData = account?.data?.raw;
    if (!rawData || account.owner.toBase58() !== PROGRAM_ID.toBase58()) {
        return onNotFound();
    }
    return <ConcurrentMerkleTreeCard data={rawData} />;
}

export default function MetaplexNFTMetadataPageClient({ params: { address } }: Props) {
    return <ParsedAccountRenderer address={address} renderComponent={ConcurrentMerkleTreeCardRenderer} />;
}


