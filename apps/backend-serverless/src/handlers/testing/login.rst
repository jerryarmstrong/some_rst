apps/backend-serverless/src/handlers/testing/login.ts
=====================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import * as Sentry from '@sentry/serverless';
import { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from 'aws-lambda';
import { createMechantAuthCookieHeader } from '../../utilities/clients/create-cookie-header.utility.js';
import { requestErrorResponse } from '../../utilities/responses/request-response.utility.js';

export const login = async (event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> => {
    Sentry.captureEvent({
        message: 'in login testing',
        level: 'info',
    });
    const testingMerchantId = 'testing-merchant-id';

    let merchantAuthCookieHeader: string;
    try {
        merchantAuthCookieHeader = createMechantAuthCookieHeader(testingMerchantId);
    } catch (error) {
        return requestErrorResponse(error);
    }

    return {
        statusCode: 200,
        headers: {
            'Set-Cookie': merchantAuthCookieHeader,
        },
        body: JSON.stringify({
            message: 'Successfully logged in.',
        }),
    };
};


