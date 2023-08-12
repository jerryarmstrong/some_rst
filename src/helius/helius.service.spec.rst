src/helius/helius.service.spec.ts
=================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { HeliusService } from './helius.service';

describe('HeliusService', () => {
  let service: HeliusService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [HeliusService],
    }).compile();

    service = module.get<HeliusService>(HeliusService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


