packages/server/src/cache.ts
============================

Last edited: 2023-01-05 08:54:11

Contents:

.. code-block:: ts

    // @ts-ignore (TS7016) There is no type definition for this at DefinitelyTyped.
import MemoryStore from 'cache-manager/lib/stores/memory';

import cacheManager from 'cache-manager';

export const cache = cacheManager.caching({ store: MemoryStore, max: 1000, ttl: 120 /*seconds*/ });


