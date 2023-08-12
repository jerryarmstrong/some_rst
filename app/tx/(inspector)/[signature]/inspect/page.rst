app/tx/(inspector)/[signature]/inspect/page.tsx
===============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { TransactionInspectorPage } from '@components/inspector/InspectorPage';
import { Metadata } from 'next/types';

type Props = Readonly<{
    params: Readonly<{
        signature: string;
    }>;
}>;

export async function generateMetadata({ params: { signature } }: Props): Promise<Metadata> {
    return {
        description: `Interactively inspect the transaction with signature ${signature} on Solana`,
        title: `Transaction Inspector | ${signature} | Solana`,
    };
}

export default function TransactionInspectionPage({ params: { signature } }: Props) {
    return <TransactionInspectorPage signature={signature} />;
}


