apps/payment-ui/src/components/handlers/WindowHandler.tsx
=========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { setPaymentMethod } from '@/features/payment-options/paymentOptionsSlice';
import { useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { AppDispatch } from '../../store';

const WindowHandler: React.FC = () => {
    const dispatch = useDispatch<AppDispatch>();

    useEffect(() => {
        const handleResize = () => {
            const isMobile = window.innerWidth < 640;
            if (isMobile) {
                dispatch(setPaymentMethod('connect-wallet'));
            }
        };

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
        };
    }, [dispatch]);

    return null;
};

export default WindowHandler;


