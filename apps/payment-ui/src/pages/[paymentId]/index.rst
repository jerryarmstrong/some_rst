apps/payment-ui/src/pages/[paymentId]/index.tsx
===============================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import CheckoutSection from '@/components/CheckoutSection';
import { DefaultLayout } from '@/components/DefaultLayout';
import FooterSection from '@/components/FooterSection';
import { useRouter } from 'next/router';

export default function CheckoutPage() {
    const router = useRouter();

    if (!router.isReady) {
        return <div>Loading...</div>;
    }

    return (
        <DefaultLayout>
            <CheckoutSection />
            <FooterSection />
        </DefaultLayout>
    );
}


