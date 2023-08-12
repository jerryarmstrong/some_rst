apps/merchant-ui/src/components/Payments.tsx
============================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import { DefaultLayoutContent } from './DefaultLayoutContent';
import { DefaultLayoutScreenTitle } from './DefaultLayoutScreenTitle';
import { PaymentsHistory } from './PaymentsHistory';

interface Props {
    className?: string;
}

export function Payments(props: Props) {
    return (
        <DefaultLayoutContent className={props.className}>
            <DefaultLayoutScreenTitle className="hidden md:block">Payments</DefaultLayoutScreenTitle>
            <DefaultLayoutScreenTitle className="block mt-8 md:hidden">Payments</DefaultLayoutScreenTitle>
            <PaymentsHistory className="mt-9" />
        </DefaultLayoutContent>
    );
}


