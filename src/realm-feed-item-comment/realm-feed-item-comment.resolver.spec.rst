src/realm-feed-item-comment/realm-feed-item-comment.resolver.spec.ts
====================================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmFeedItemCommentResolver } from './realm-feed-item-comment.resolver';

describe('RealmFeedItemCommentResolver', () => {
  let resolver: RealmFeedItemCommentResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmFeedItemCommentResolver],
    }).compile();

    resolver = module.get<RealmFeedItemCommentResolver>(RealmFeedItemCommentResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


