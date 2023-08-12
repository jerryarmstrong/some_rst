src/discord/discord.module.ts
=============================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Module } from '@nestjs/common';

import { ConfigModule } from '@src/config/config.module';

import { DiscordService } from './discord.service';

@Module({
  imports: [ConfigModule],
  providers: [DiscordService],
  exports: [DiscordService],
})
export class DiscordModule {}


