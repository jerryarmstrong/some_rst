src/realm/realm.resolver.spec.ts
================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmResolver } from './realm.resolver';
import { RealmService } from './realm.service';

describe('RealmResolver', () => {
  let resolver: RealmResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmResolver, RealmService],
    }).compile();

    resolver = module.get<RealmResolver>(RealmResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


