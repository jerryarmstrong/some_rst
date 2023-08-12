apps/payment-ui/src/components/handlers/CompletingHandler.tsx
=============================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { getIsCompleting, setCompleted } from '@/features/payment-session/paymentSessionSlice';
import { useEffect, useRef } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { AppDispatch } from '../../store';

const CompletingHandler: React.FC = () => {
    const dispatch = useDispatch<AppDispatch>();
    const isCompleting = useSelector(getIsCompleting);
    let timer = useRef<any | null>(null);

    useEffect(() => {
        if (isCompleting) {
            const interval = 500;

            timer.current = setInterval(() => {
                clearInterval(timer.current);
                dispatch(setCompleted());
            }, interval);
        }

        return () => {};
    }, [dispatch, isCompleting]);

    return null;
};

export default CompletingHandler;


