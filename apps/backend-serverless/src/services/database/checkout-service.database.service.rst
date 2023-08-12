apps/backend-serverless/src/services/database/checkout-service.database.service.ts
==================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { Checkout, PrismaClient } from '@prisma/client';
import { prismaErrorHandler } from './shared.database.service.js';

export class CheckoutService {
    private prisma: PrismaClient;

    constructor(prismaClient: PrismaClient) {
        this.prisma = prismaClient;
    }

    async createOrUpdateCheckout(checkoutToken: string, productIds: string): Promise<Checkout> {
        let checkout;
        const existingCheckout = await this.prisma.checkout.findUnique({
            where: { checkoutToken: checkoutToken },
        });

        if (existingCheckout) {
            checkout = await this.prisma.checkout.update({
                where: { checkoutToken: checkoutToken },
                data: { productIds: productIds },
            });
        } else {
            checkout = await this.prisma.checkout.create({
                data: { checkoutToken: checkoutToken, productIds: productIds },
            });
        }

        return checkout;
    }

    async getProductsInCheckout(checkoutToken: string): Promise<string[]> {
        const productIds = await prismaErrorHandler(
            this.prisma.checkout.findUnique({
                where: { checkoutToken: checkoutToken },
            })
        );

        if (productIds == null) {
            return [];
        }

        return productIds.productIds.split(',');
    }
}


