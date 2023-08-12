src/stats/stats.controller.ts
=============================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Controller, Get, Query } from '@nestjs/common';

import { StatsService } from './stats.service';

@Controller('stats')
export class StatsController {
  constructor(private readonly statsService: StatsService) {}

  @Get('/tvl')
  getTvl(@Query('force') force?: string) {
    return this.statsService.getTvl(force?.toLocaleLowerCase() === 'true');
  }
}


