apps/payment-ui/src/components/PayToLabel/PayToDisplay.tsx
==========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    export const PayToDisplay = (props: { merchantName: string }) => {
    return <div className="text-2xl">{'Pay to ' + props.merchantName}</div>;
};

export const PayToLoading = () => {
    return (
        <div className="animate-pulse flex items-center justify-start">
            <div className="rounded-full bg-gray-200 h-6 w-44" />
        </div>
    );
};


