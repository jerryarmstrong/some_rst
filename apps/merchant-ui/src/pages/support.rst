apps/merchant-ui/src/pages/support.tsx
======================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { DefaultLayout } from '@/components/DefaultLayout';
import { SupportFaq } from '@/components/SupportFaq';
import Head from 'next/head';

export default function Support() {
    return (
        <>
            <Head>
                <title>Solana Pay - Support</title>
                <meta name="description" content="Support" />
            </Head>
            <div className="h-screen w-screen">
                <DefaultLayout className="h-full w-full">
                    <SupportFaq />
                </DefaultLayout>
            </div>
        </>
    );
}


