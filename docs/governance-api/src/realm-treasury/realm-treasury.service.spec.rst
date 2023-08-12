src/realm-treasury/realm-treasury.service.spec.ts
=================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmTreasuryService } from './realm-treasury.service';

describe('RealmTreasuryService', () => {
  let service: RealmTreasuryService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmTreasuryService],
    }).compile();

    service = module.get<RealmTreasuryService>(RealmTreasuryService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


