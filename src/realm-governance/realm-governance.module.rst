src/realm-governance/realm-governance.module.ts
===============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Module } from '@nestjs/common';

import { HeliusModule } from '@src/helius/helius.module';
import { StaleCacheModule } from '@src/stale-cache/stale-cache.module';

import { RealmGovernanceService } from './realm-governance.service';

@Module({
  imports: [HeliusModule, StaleCacheModule],
  providers: [RealmGovernanceService],
  exports: [RealmGovernanceService],
})
export class RealmGovernanceModule {}


