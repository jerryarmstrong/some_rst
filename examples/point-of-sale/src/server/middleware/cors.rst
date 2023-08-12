examples/point-of-sale/src/server/middleware/cors.ts
====================================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import expressCors from 'cors';
import { wrapExpressHandler } from './wrapExpressHandler';

export const cors = wrapExpressHandler(expressCors({ origin: true, methods: ['POST'] }));


