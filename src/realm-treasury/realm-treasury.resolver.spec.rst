src/realm-treasury/realm-treasury.resolver.spec.ts
==================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmTreasuryResolver } from './realm-treasury.resolver';

describe('RealmTreasuryResolver', () => {
  let resolver: RealmTreasuryResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmTreasuryResolver],
    }).compile();

    resolver = module.get<RealmTreasuryResolver>(RealmTreasuryResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


