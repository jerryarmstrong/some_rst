apps/payment-ui/src/components/handlers/RouterHandler.tsx
=========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { setPaymentId } from '@/features/payment-details/paymentDetailsSlice';
import { setWebsocketReadyToConnect } from '@/features/websocket/websocketSlice';
import { useRouter } from 'next/router';
import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { AppDispatch } from '../../store';

const RouterHandler: React.FC = () => {
    const dispatch = useDispatch<AppDispatch>();
    const router = useRouter();

    const paymentId = router.query.paymentId as string;

    useEffect(() => {
        if (!router.isReady) {
            return;
        }

        dispatch(setPaymentId(paymentId));
        dispatch(setWebsocketReadyToConnect());
    }, [router.isReady, paymentId, dispatch]);

    return null;
};

export default RouterHandler;


