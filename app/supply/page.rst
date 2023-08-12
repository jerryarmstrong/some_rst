app/supply/page.tsx
===================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import SupplyPageClient from './page-client';

export const metadata = {
    description: `Overview of the native token supply on Solana`,
    title: `Supply Overview | Solana`,
};

export default function SupplyPage() {
    return <SupplyPageClient />;
}


