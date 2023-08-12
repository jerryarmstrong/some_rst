src/realm-proposal/realm-proposal.service.spec.ts
=================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmProposalService } from './realm-proposal.service';

describe('RealmProposalService', () => {
  let service: RealmProposalService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmProposalService],
    }).compile();

    service = module.get<RealmProposalService>(RealmProposalService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


