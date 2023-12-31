apps/mock-shopify-serverless/src/handlers/payment.ts
====================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from 'aws-lambda';
import axios from 'axios';

function getRandomArbitrary(min: number, max: number): number {
    return Math.random() * (max - min) + min;
}

export const payment = async (event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> => {
    const id = getRandomArbitrary(1, 1000000).toString();
    const gid = getRandomArbitrary(1, 1000000).toString();
    const group = getRandomArbitrary(1, 1000000).toString();

    try {
        const response = await axios({
            url: 'http://localhost:4006/payment',
            method: 'POST',
            headers: {
                'shopify-shop-domain': 'localhost:4004',
                'shopify-request-id': '123',
                'shopify-api-version': '2021-07',
            },
            data: JSON.stringify({
                id: id,
                gid: gid,
                group: group,
                amount: 11,
                currency: 'USD',
                test: true,
                merchant_locale: 'en',
                payment_method: {
                    type: 'type',
                    data: {
                        cancel_url: 'localhost:4004/c1-7743a01d14a69841e687352c38c7a0e0',
                    },
                },
                proposed_at: '2021-08-10T18:02:00.000Z',
                kind: 'payment',
                customer: null,
            }),
        });

        const redirect_url = response.data.redirect_url;

        return {
            statusCode: 302,
            headers: {
                Location: redirect_url,
                'Content-Type': 'text/html',
            },
            body: JSON.stringify({}),
        };
    } catch (error) {
        return {
            statusCode: 200,
            body: JSON.stringify(error),
        };
    }
};


