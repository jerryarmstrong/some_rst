src/ecosystem-feed/ecosystem-feed.service.spec.ts
=================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { EcosystemFeedService } from './ecosystem-feed.service';

describe('EcosystemFeedService', () => {
  let service: EcosystemFeedService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [EcosystemFeedService],
    }).compile();

    service = module.get<EcosystemFeedService>(EcosystemFeedService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


