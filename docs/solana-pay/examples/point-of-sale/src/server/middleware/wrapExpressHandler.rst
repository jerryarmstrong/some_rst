examples/point-of-sale/src/server/middleware/wrapExpressHandler.ts
==================================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import { RequestHandler } from 'express';
import { NextApiHandler, NextApiRequest, NextApiResponse } from 'next';

// Wrap an Express middleware function for compatibility with Next
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


