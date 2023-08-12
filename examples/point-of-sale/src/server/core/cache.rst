examples/point-of-sale/src/server/core/cache.ts
===============================================

Last edited: 2023-05-03 15:27:33

Contents:

.. code-block:: ts

    import cacheManager from 'cache-manager';
// @ts-ignore (TS7016) There is no type definition for this at DefinitelyTyped.
import MemoryStore from 'cache-manager/lib/stores/memory';

export const cache = cacheManager.caching({ store: MemoryStore, max: 1000, ttl: 120 /*seconds*/ });


