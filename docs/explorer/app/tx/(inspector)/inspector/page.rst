app/tx/(inspector)/inspector/page.tsx
=====================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { TransactionInspectorPage } from '@components/inspector/InspectorPage';

type Props = Readonly<{
    params: Readonly<{
        signature: string;
    }>;
}>;

export default function Page({ params: { signature } }: Props) {
    return <TransactionInspectorPage signature={signature} />;
}


