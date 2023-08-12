src/follow-feed/follow-feed.resolver.spec.ts
============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { FollowFeedResolver } from './follow-feed.resolver';

describe('FollowFeedResolver', () => {
  let resolver: FollowFeedResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [FollowFeedResolver],
    }).compile();

    resolver = module.get<FollowFeedResolver>(FollowFeedResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


