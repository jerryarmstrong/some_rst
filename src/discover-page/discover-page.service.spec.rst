src/discover-page/discover-page.service.spec.ts
===============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { DiscoverPageService } from './discover-page.service';

describe('DiscoverPageService', () => {
  let service: DiscoverPageService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [DiscoverPageService],
    }).compile();

    service = module.get<DiscoverPageService>(DiscoverPageService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


