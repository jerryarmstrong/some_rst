apps/merchant-ui/src/lib/endpoints.ts
=====================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export const API_ENDPOINTS = {
    install: `${process.env.NEXT_PUBLIC_API_BASE_URL}/install`,
    logout: `${process.env.NEXT_PUBLIC_API_BASE_URL}/logout`,
    redirect: `${process.env.NEXT_PUBLIC_API_BASE_URL}/redirect`,
    payment: `${process.env.NEXT_PUBLIC_API_BASE_URL}/payment`,
    refund: `${process.env.NEXT_PUBLIC_API_BASE_URL}/refund`,
    paymentTransaction: `${process.env.NEXT_PUBLIC_API_BASE_URL}/payment-transaction`,
    refundTransaction: `${process.env.NEXT_PUBLIC_API_BASE_URL}/refund-transaction`,
    pointsSetupTransaction: `${process.env.NEXT_PUBLIC_API_BASE_URL}/points-setup-transaction`,
    rejectRefund: `${process.env.NEXT_PUBLIC_API_BASE_URL}/reject-refund`,
    merchantData: `${process.env.NEXT_PUBLIC_API_BASE_URL}/merchant-data`,
    refundData: `${process.env.NEXT_PUBLIC_API_BASE_URL}/refund-data`,
    refundStatus: `${process.env.NEXT_PUBLIC_API_BASE_URL}/refund-status`,
    paymentData: `${process.env.NEXT_PUBLIC_API_BASE_URL}/payment-data`,
    updateMerchant: `${process.env.NEXT_PUBLIC_API_BASE_URL}/update-merchant`,
    updateLoyalty: `${process.env.NEXT_PUBLIC_API_BASE_URL}/update-loyalty`,
    loyaltyData: `${process.env.NEXT_PUBLIC_API_BASE_URL}/loyalty-data`,
    manageTiers: `${process.env.NEXT_PUBLIC_API_BASE_URL}/manage-tiers`,
    manageProducts: `${process.env.NEXT_PUBLIC_API_BASE_URL}/manage-products`,
};


