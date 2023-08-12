src/realm-feed/realm-feed.resolver.spec.ts
==========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmFeedResolver } from './realm-feed.resolver';
import { RealmFeedService } from './realm-feed.service';

describe('RealmFeedResolver', () => {
  let resolver: RealmFeedResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmFeedResolver, RealmFeedService],
    }).compile();

    resolver = module.get<RealmFeedResolver>(RealmFeedResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


