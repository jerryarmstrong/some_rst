apps/mock-shopify-serverless/src/handlers/access-token.ts
=========================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from 'aws-lambda';

export const accessToken = async (event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> => {
    return {
        statusCode: 200,
        body: JSON.stringify({
            access_token: 'a-lil-mf-access-token-or-whatever',
            scope: 'write_payment_gateways,write_payment_sessions',
        }),
    };
};


