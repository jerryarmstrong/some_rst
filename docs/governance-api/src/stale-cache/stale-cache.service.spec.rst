src/stale-cache/stale-cache.service.spec.ts
===========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { StaleCacheService } from './stale-cache.service';

describe('StaleCacheService', () => {
  let service: StaleCacheService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [StaleCacheService],
    }).compile();

    service = module.get<StaleCacheService>(StaleCacheService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


