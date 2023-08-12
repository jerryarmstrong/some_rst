backend/workers/price-indexer/src/index.ts
==========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { fetchHandler } from "./fetched";
import { scheduledHandler } from "./scheduled";
import type { Environment } from "./types";

const handler: ExportedHandler<Environment> = {
  fetch: fetchHandler,
  scheduled: scheduledHandler,
};

export default handler;


