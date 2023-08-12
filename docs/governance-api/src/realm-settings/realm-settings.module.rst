src/realm-settings/realm-settings.module.ts
===========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { CacheModule, Module } from '@nestjs/common';

import { ConfigModule } from '@src/config/config.module';
import { StaleCacheModule } from '@src/stale-cache/stale-cache.module';

import { RealmSettingsService } from './realm-settings.service';

@Module({
  imports: [CacheModule.register(), ConfigModule, StaleCacheModule],
  providers: [RealmSettingsService],
  exports: [RealmSettingsService],
})
export class RealmSettingsModule {}


