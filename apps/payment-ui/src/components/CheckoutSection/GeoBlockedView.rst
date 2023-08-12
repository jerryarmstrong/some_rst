apps/payment-ui/src/components/CheckoutSection/GeoBlockedView.tsx
=================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { getPaymentDetails } from '@/features/payment-details/paymentDetailsSlice';
import { useSelector } from 'react-redux';
import { ErrorView } from './ErrorView';

export const GeoBlockedView = () => {
    const paymentDetails = useSelector(getPaymentDetails);

    const error = {
        top: 'GeoBlocked',
        bottom: 'Sorry, we are not allowed to operate in your jurisdiction',
        redirect: paymentDetails?.cancelUrl ?? null,
    };

    return <ErrorView error={error} />;
};


