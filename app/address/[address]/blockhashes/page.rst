app/address/[address]/blockhashes/page.tsx
==========================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import RecentBlockhashesPageClient from './page-client';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

export const metadata = {
    description: `Recent blockhashes on Solana`,
    title: `Recent Blockhashes | Solana`,
};

export default function RecentBlockhashesPage(props: Props) {
    return <RecentBlockhashesPageClient {...props} />;
}


