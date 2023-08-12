src/app.controller.ts
=====================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Controller, Get } from '@nestjs/common';

import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}


