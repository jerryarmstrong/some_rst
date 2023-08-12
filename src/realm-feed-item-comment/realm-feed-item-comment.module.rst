src/realm-feed-item-comment/realm-feed-item-comment.module.ts
=============================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Module, forwardRef } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';

import { ConfigModule } from '@src/config/config.module';
import { DialectModule } from '@src/dialect/dialect.module';
import { RealmFeedItem } from '@src/realm-feed-item/entities/RealmFeedItem.entity';
import { RealmMemberModule } from '@src/realm-member/realm-member.module';
import { RealmPost } from '@src/realm-post/entities/RealmPost.entity';
import { RealmModule } from '@src/realm/realm.module';

import { RealmFeedItemComment } from './entities/RealmFeedItemComment.entity';
import { RealmFeedItemCommentVote } from './entities/RealmFeedItemCommentVote.entity';
import { RealmFeedItemCommentResolver } from './realm-feed-item-comment.resolver';
import { RealmFeedItemCommentService } from './realm-feed-item-comment.service';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      RealmFeedItem,
      RealmFeedItemComment,
      RealmFeedItemCommentVote,
      RealmPost,
    ]),
    RealmMemberModule,
    ConfigModule,
    DialectModule,
    forwardRef(() => RealmModule),
  ],
  providers: [RealmFeedItemCommentService, RealmFeedItemCommentResolver],
  exports: [RealmFeedItemCommentService],
})
export class RealmFeedItemCommentModule {}


