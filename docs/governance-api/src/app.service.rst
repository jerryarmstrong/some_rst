src/app.service.ts
==================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }
}


