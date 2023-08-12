src/discover-page/discover-page.resolver.spec.ts
================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { DiscoverPageResolver } from './discover-page.resolver';

describe('DiscoverPageResolver', () => {
  let resolver: DiscoverPageResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [DiscoverPageResolver],
    }).compile();

    resolver = module.get<DiscoverPageResolver>(DiscoverPageResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


