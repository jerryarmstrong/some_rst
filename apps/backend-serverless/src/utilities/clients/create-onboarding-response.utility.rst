apps/backend-serverless/src/utilities/clients/create-onboarding-response.utility.ts
===================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { KybState, Merchant } from '@prisma/client';

export interface OnboardingResponse {
    completed: boolean;
    acceptedTermsAndConditions: boolean;
    acceptedPrivacyPolicy: boolean;
    addedWallet: boolean;
    dismissedCompleted: boolean;
    kybState: KybState;
}

export const createOnboardingResponse = (merchant: Merchant) => {
    const shopifyClientId = process.env.SHOPIFY_CLIENT_ID;

    const acceptedTermsAndConditions = merchant.acceptedTermsAndConditions;
    const acceptedPrivacyPolicy = merchant.acceptedPrivacyPolicy;
    const addedWallet = merchant.walletAddress != null || merchant.tokenAddress != null;
    const kybState = merchant.kybState;
    const dismissCompleted = merchant.dismissCompleted;

    const redirectURL = `https://${merchant.shop}/services/payments_partners/gateways/${shopifyClientId}/settings`;

    return {
        completed:
            acceptedTermsAndConditions &&
            acceptedPrivacyPolicy &&
            dismissCompleted &&
            addedWallet &&
            kybState == 'finished',
        acceptedTermsAndConditions: acceptedTermsAndConditions,
        acceptedPrivacyPolicy: acceptedPrivacyPolicy,
        addedWallet: addedWallet,
        dismissedCompleted: dismissCompleted,
        kybState: kybState,
        completedRedirect: redirectURL,
    };
};


