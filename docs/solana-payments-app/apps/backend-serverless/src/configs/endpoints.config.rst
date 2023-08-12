apps/backend-serverless/src/configs/endpoints.config.ts
=======================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    export const shopifyGraphQLEndpoint = (shopDomain: string) => {
    return `https://${shopDomain}/payments_apps/api/2022-10/graphql.json`;
};

export const shopifyAdminGraphQLEndpoint = (shopDomain: string) => {
    return `https://${shopDomain}/admin/api/2022-10/graphql.json`;
};

export const shopifyAdminRestEndpoint = (shopDomain: string, resource: string) => {
    return `https://${shopDomain}/admin/api/2022-10/${resource}.json`;
};


