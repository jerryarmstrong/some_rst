src/follow-feed/follow-feed.service.spec.ts
===========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { FollowFeedService } from './follow-feed.service';

describe('FollowFeedService', () => {
  let service: FollowFeedService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [FollowFeedService],
    }).compile();

    service = module.get<FollowFeedService>(FollowFeedService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


