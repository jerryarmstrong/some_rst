apps/merchant-ui/src/pages/loyalty.tsx
======================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { DefaultLayout } from '@/components/DefaultLayout';
import { LoyaltyScreen } from '@/components/LoyaltyScreen';
import Merchant404 from '@/components/Merchant404';
import { isFailed, isOk } from '@/lib/Result';
import { useMerchantStore } from '@/stores/merchantStore';
import Head from 'next/head';
import Router from 'next/router';

export default function Loyalty() {
    const merchantInfo = useMerchantStore(state => state.merchantInfo);
    if (isFailed(merchantInfo)) {
        return <Merchant404 />;
    }

    if (isOk(merchantInfo) && !merchantInfo.data.completed) {
        Router.push('/getting-started');
    }

    return (
        <>
            <Head>
                <title>Solana Pay - Loyalty</title>
                <meta name="description" content="Manage your Shopify Loyalty program" />
            </Head>
            <div className="h-screen w-screen">
                <DefaultLayout accountIsActive className="h-full w-full">
                    <LoyaltyScreen />
                </DefaultLayout>
            </div>
        </>
    );
}


