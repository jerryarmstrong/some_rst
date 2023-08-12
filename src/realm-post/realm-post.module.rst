src/realm-post/realm-post.module.ts
===================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';

import { RealmPost } from './entities/RealmPost.entity';
import { RealmPostResolver } from './realm-post.resolver';
import { RealmPostService } from './realm-post.service';

@Module({
  imports: [TypeOrmModule.forFeature([RealmPost])],
  providers: [RealmPostResolver, RealmPostService],
  exports: [RealmPostService],
})
export class RealmPostModule {}


