apps/backend-serverless/src/services/database/gdpr-service.database.service.ts
==============================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { GDPR, PrismaClient } from '@prisma/client';
import { prismaErrorHandler } from './shared.database.service.js';

export class GDPRService {
    private prisma: PrismaClient;

    constructor(prismaClient: PrismaClient) {
        this.prisma = prismaClient;
    }

    async createGDPRRequest(merchantId: string): Promise<GDPR> {
        return prismaErrorHandler(
            this.prisma.gDPR.create({
                data: {
                    merchantId: merchantId,
                    completed: false,
                },
            }),
        );
    }
}


