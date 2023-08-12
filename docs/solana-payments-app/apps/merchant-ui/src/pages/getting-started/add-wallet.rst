apps/merchant-ui/src/pages/getting-started/add-wallet.tsx
=========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { DefaultLayout } from '@/components/DefaultLayout';
import { GettingStartedAddWallet } from '@/components/GettingStartedAddWallet';
import Head from 'next/head';

export default function AddWallet() {
    return (
        <>
            <Head>
                <title>Solana Pay - Add a wallet</title>
                <meta name="description" content="Add a wallet" />
            </Head>
            <div className="h-screen w-screen">
                <DefaultLayout className="h-full w-full">
                    <GettingStartedAddWallet />
                </DefaultLayout>
            </div>
        </>
    );
}


