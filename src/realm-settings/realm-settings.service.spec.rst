src/realm-settings/realm-settings.service.spec.ts
=================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmSettingsService } from './realm-settings.service';

describe('RealmSettingsService', () => {
  let service: RealmSettingsService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmSettingsService],
    }).compile();

    service = module.get<RealmSettingsService>(RealmSettingsService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


