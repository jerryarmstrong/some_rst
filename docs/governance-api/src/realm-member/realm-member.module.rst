src/realm-member/realm-member.module.ts
=======================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { CacheModule, Module } from '@nestjs/common';

import { ConfigModule } from '@src/config/config.module';
import { HeliusModule } from '@src/helius/helius.module';
import { StaleCacheModule } from '@src/stale-cache/stale-cache.module';

import { RealmMemberResolver } from './realm-member.resolver';
import { RealmMemberService } from './realm-member.service';

@Module({
  imports: [CacheModule.register(), ConfigModule, HeliusModule, StaleCacheModule],
  providers: [RealmMemberResolver, RealmMemberService],
  exports: [RealmMemberService],
})
export class RealmMemberModule {}


