src/discord-user/discordUser.module.ts
======================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';

import { ConfigModule } from '@src/config/config.module';

import { DiscordUserController } from './discordUser.controller';
import { DiscordUserResolver } from './discordUser.resolver';
import { DiscordUserService } from './discordUser.service';
import { DiscordUser } from './entities/DiscordUser.entity';
import { MatchdayDiscordUser } from './entities/MatchdayDiscordUser.entity';
import { MatchdayDiscordUserController } from './matchdayDiscordUser.controller';
import { MatchdayDiscordUserService } from './matchdayDiscordUser.service';

@Module({
  imports: [TypeOrmModule.forFeature([DiscordUser, MatchdayDiscordUser]), ConfigModule],
  controllers: [DiscordUserController, MatchdayDiscordUserController],
  providers: [DiscordUserResolver, DiscordUserService, MatchdayDiscordUserService],
  exports: [DiscordUserService],
})
export class DiscordUserModule {}


