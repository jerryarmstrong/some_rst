apps/backend-serverless/src/handlers/clients/merchant-ui/read-data/refund-status.ts
===================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { PrismaClient } from '@prisma/client';
import * as Sentry from '@sentry/serverless';
import { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from 'aws-lambda';
import { parseAndValidateRefundStatusRequest } from '../../../../models/clients/merchant-ui/refund-status-request.model.js';
import { RefundRecordService } from '../../../../services/database/refund-record-service.database.service.js';
import { createGeneralResponse } from '../../../../utilities/clients/create-general-response.js';
import { createRefundDataResponseFromRefundRecord } from '../../../../utilities/clients/refund-record.utility.js';
import { withAuth } from '../../../../utilities/clients/token-authenticate.utility.js';
import { createErrorResponse } from '../../../../utilities/responses/error-response.utility.js';

const prisma = new PrismaClient();

Sentry.AWSLambda.init({
    dsn: process.env.SENTRY_DSN,
    tracesSampleRate: 1.0,
    integrations: [new Sentry.Integrations.Prisma({ client: prisma })],
});

export const refundStatus = Sentry.AWSLambda.wrapHandler(
    async (event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> => {
        const refundRecordService = new RefundRecordService(prisma);

        Sentry.captureEvent({
            message: 'in refund-status',
            level: 'info',
        });

        try {
            const merchantAuthToken = withAuth(event.cookies);
            const refundStatusRequestParameters = parseAndValidateRefundStatusRequest(event.queryStringParameters);

            const refundRecord = await refundRecordService.getRefundRecordWithPayment({
                shopId: refundStatusRequestParameters.shopId,
            });

            const refundStatusResponse = createRefundDataResponseFromRefundRecord(refundRecord);
            const generalResponse = await createGeneralResponse(merchantAuthToken, prisma);
            const responseBodyData = {
                refundStatus: refundStatusResponse,
                general: generalResponse,
            };

            return {
                statusCode: 200,
                body: JSON.stringify(responseBodyData),
            };
        } catch (error) {
            return createErrorResponse(error);
        }
    },
    {
        rethrowAfterCapture: false,
    }
);


