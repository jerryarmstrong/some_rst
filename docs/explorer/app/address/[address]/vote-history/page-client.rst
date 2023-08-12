app/address/[address]/vote-history/page-client.tsx
==================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    'use client';

import { ParsedAccountRenderer } from '@components/account/ParsedAccountRenderer';
import { VotesCard } from '@components/account/VotesCard';
import React from 'react';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

function VotesCardRenderer({
    account,
    onNotFound,
}: React.ComponentProps<React.ComponentProps<typeof ParsedAccountRenderer>['renderComponent']>) {
    const parsedData = account?.data?.parsed;
    if (!parsedData || parsedData?.program !== 'vote') {
        return onNotFound();
    }
    return <VotesCard voteAccount={parsedData.parsed} />;
}

export default function VoteHistoryPageClient({ params: { address } }: Props) {
    return <ParsedAccountRenderer address={address} renderComponent={VotesCardRenderer} />;
}


