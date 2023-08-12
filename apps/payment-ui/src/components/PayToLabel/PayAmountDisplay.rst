apps/payment-ui/src/components/PayToLabel/PayAmountDisplay.tsx
==============================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    export const PayAmountDisplay = (props: { amount: number }) => {
    return <div className="text-5xl">${props.amount.toFixed(2)}</div>;
};

export const PayAmountLoading = () => {
    return (
        <div className="animate-pulse flex items-center justify-start">
            <div className="rounded-full bg-gray-200 h-10 w-64" />
        </div>
    );
};


