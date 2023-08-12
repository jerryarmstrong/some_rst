app/address/[address]/slot-hashes/page.tsx
==========================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import SlotHashesPageClient from './page-client';

type Props = Readonly<{
    params: {
        address: string;
    };
}>;

export const metadata = {
    description: `Hashes of each slot on Solana`,
    title: `Slot Hashes | Solana`,
};

export default function SlotHashesPage(props: Props) {
    return <SlotHashesPageClient {...props} />;
}


