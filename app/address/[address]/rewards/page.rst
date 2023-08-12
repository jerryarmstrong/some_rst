app/address/[address]/rewards/page.tsx
======================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { RewardsCard } from '@components/account/RewardsCard';
import getReadableTitleFromAddress, { AddressPageMetadataProps } from '@utils/get-readable-title-from-address';
import { Metadata } from 'next/types';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

export async function generateMetadata(props: AddressPageMetadataProps): Promise<Metadata> {
    return {
        description: `Rewards due to the address ${props.params.address} by epoch on Solana`,
        title: `Address Rewards | ${await getReadableTitleFromAddress(props)} | Solana`,
    };
}

export default function BlockRewardsPage({ params: { address } }: Props) {
    return <RewardsCard address={address} />;
}


