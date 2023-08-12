src/ecosystem-feed/ecosystem-feed.resolver.spec.ts
==================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { EcosystemFeedResolver } from './ecosystem-feed.resolver';

describe('EcosystemFeedResolver', () => {
  let resolver: EcosystemFeedResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [EcosystemFeedResolver],
    }).compile();

    resolver = module.get<EcosystemFeedResolver>(EcosystemFeedResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


