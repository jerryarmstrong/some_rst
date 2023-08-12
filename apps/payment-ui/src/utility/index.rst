apps/payment-ui/src/utility/index.ts
====================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export const convertToDollarString = (amount: number): string => {
    return `$${(amount / 100).toFixed(2)}`;
};


