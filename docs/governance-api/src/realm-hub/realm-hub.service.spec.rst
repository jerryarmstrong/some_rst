src/realm-hub/realm-hub.service.spec.ts
=======================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmHubService } from './realm-hub.service';

describe('RealmHubService', () => {
  let service: RealmHubService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmHubService],
    }).compile();

    service = module.get<RealmHubService>(RealmHubService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


