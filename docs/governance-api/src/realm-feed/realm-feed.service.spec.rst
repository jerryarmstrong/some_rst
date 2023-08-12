src/realm-feed/realm-feed.service.spec.ts
=========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmFeedService } from './realm-feed.service';

describe('RealmFeedService', () => {
  let service: RealmFeedService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmFeedService],
    }).compile();

    service = module.get<RealmFeedService>(RealmFeedService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


