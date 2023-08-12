packages/server/src/middleware/cors.ts
======================================

Last edited: 2023-01-05 08:54:11

Contents:

.. code-block:: ts

    import expressCors from 'cors';
import config from '../../../../config.json';
import { wrapExpressHandler } from './wrapExpressHandler';

export const cors = wrapExpressHandler(expressCors({ origin: config.corsOrigin, methods: ['GET', 'POST', 'OPTIONS'] }));


