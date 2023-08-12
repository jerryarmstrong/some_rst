src/realm-post/realm-post.service.spec.ts
=========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmPostService } from './realm-post.service';

describe('RealmPostService', () => {
  let service: RealmPostService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmPostService],
    }).compile();

    service = module.get<RealmPostService>(RealmPostService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


