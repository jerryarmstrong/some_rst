src/config/config.service.spec.ts
=================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import type { TestingModule } from '@nestjs/testing';
import { Test } from '@nestjs/testing';

import { ConfigService } from './config.service';

describe('ConfigService', () => {
  let service: ConfigService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [ConfigService],
    }).compile();

    service = module.get<ConfigService>(ConfigService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


