app/address/[address]/stake-history/page.tsx
============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import StakeHistoryPageClient from './page-client';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

export const metadata = {
    description: `Stake history for each epoch on Solana`,
    title: `Stake History | Solana`,
};

export default function StakeHistoryPage(props: Props) {
    return <StakeHistoryPageClient {...props} />;
}


