src/realm-feed-item/realm-feed-item.resolver.spec.ts
====================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmFeedItemResolver } from './realm-feed-item.resolver';
import { RealmFeedItemService } from './realm-feed-item.service';

describe('RealmFeedItemResolver', () => {
  let resolver: RealmFeedItemResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmFeedItemResolver, RealmFeedItemService],
    }).compile();

    resolver = module.get<RealmFeedItemResolver>(RealmFeedItemResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


