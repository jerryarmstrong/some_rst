apps/merchant-ui/src/pages/termsofservice.tsx
=============================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { DefaultLayout } from '@/components/DefaultLayout';
import { DefaultLayoutContent } from '@/components/DefaultLayoutContent';
import { DefaultLayoutScreenTitle } from '@/components/DefaultLayoutScreenTitle';
import { PdfViewer } from '@/components/PdfViewer';
import Head from 'next/head';

const title = 'Terms of Service';

export default function TermsOfService() {
    return (
        <>
            <Head>
                <title>Solana Pay - {title}</title>
                <meta name="description" content={title} />
            </Head>
            <div className="h-screen w-screen">
                <DefaultLayout className="h-full w-full">
                    <DefaultLayoutContent>
                        <DefaultLayoutScreenTitle>{title}</DefaultLayoutScreenTitle>
                        <PdfViewer title={'Terms of Service'} />
                    </DefaultLayoutContent>
                </DefaultLayout>
            </div>
        </>
    );
}


