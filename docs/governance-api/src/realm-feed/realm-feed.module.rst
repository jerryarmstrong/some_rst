src/realm-feed/realm-feed.module.ts
===================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Module } from '@nestjs/common';

import { RealmFeedItemModule } from '@src/realm-feed-item/realm-feed-item.module';
import { RealmProposalModule } from '@src/realm-proposal/realm-proposal.module';

import { RealmFeedResolver } from './realm-feed.resolver';
import { RealmFeedService } from './realm-feed.service';

@Module({
  imports: [RealmFeedItemModule, RealmProposalModule],
  providers: [RealmFeedResolver, RealmFeedService],
  exports: [RealmFeedService],
})
export class RealmFeedModule {}


