packages/server/src/middleware/wrapExpressHandler.ts
====================================================

Last edited: 2023-01-05 08:54:11

Contents:

.. code-block:: ts

    import type { NextApiHandler, NextApiRequest, NextApiResponse } from 'next';
import { RequestHandler } from 'express';

// Wrap an Express middleware function for compatibility with Vercel
export const wrapExpressHandler = function (handler: RequestHandler): NextApiHandler {
    return function (request: NextApiRequest, response: NextApiResponse): Promise<void> {
        return new Promise<void>(function (resolve, reject) {
            handler(request as any, response as any, function (error?: any) {
                if (error) {
                    reject(error);
                } else {
                    resolve();
                }
            });
        });
    };
};


