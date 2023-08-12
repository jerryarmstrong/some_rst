src/realm-feed-item-comment/realm-feed-item-comment.service.spec.ts
===================================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmFeedItemCommentService } from './realm-feed-item-comment.service';

describe('RealmFeedItemCommentService', () => {
  let service: RealmFeedItemCommentService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmFeedItemCommentService],
    }).compile();

    service = module.get<RealmFeedItemCommentService>(RealmFeedItemCommentService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


