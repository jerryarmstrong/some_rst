src/realm-hub/realm-hub.resolver.spec.ts
========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmHubResolver } from './realm-hub.resolver';

describe('RealmHubResolver', () => {
  let resolver: RealmHubResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmHubResolver],
    }).compile();

    resolver = module.get<RealmHubResolver>(RealmHubResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


