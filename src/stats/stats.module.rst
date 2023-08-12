src/stats/stats.module.ts
=========================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';

import { HeliusModule } from '@src/helius/helius.module';
import { Realm } from '@src/realm/entities/Realm.entity';

import { Tvl } from './entities/Tvl.entity';
import { StatsController } from './stats.controller';
import { StatsService } from './stats.service';

@Module({
  imports: [HeliusModule, TypeOrmModule.forFeature([Realm, Tvl])],
  providers: [StatsService],
  controllers: [StatsController],
})
export class StatsModule {}


