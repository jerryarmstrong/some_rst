src/stale-cache/stale-cache.module.ts
=====================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { CacheModule, Module } from '@nestjs/common';

import { StaleCacheService } from './stale-cache.service';

@Module({
  imports: [CacheModule.register()],
  providers: [StaleCacheService],
  exports: [StaleCacheService],
})
export class StaleCacheModule {}


