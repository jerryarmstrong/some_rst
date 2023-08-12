src/realm-member/realm-member.service.spec.ts
=============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { RealmMemberService } from './realm-member.service';

describe('RealmMemberService', () => {
  let service: RealmMemberService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [RealmMemberService],
    }).compile();

    service = module.get<RealmMemberService>(RealmMemberService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});


