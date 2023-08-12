src/realm-governance/realm-governance.service.spec.ts
=====================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmGovernanceService } from './realm-governance.service';

describe('RealmGovernanceService', () => {
  let service: RealmGovernanceService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmGovernanceService],
    }).compile();

    service = module.get<RealmGovernanceService>(RealmGovernanceService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


