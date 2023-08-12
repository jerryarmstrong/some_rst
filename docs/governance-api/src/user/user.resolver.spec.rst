src/user/user.resolver.spec.ts
==============================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Test, TestingModule } from '@nestjs/testing';

import { UserResolver } from './user.resolver';
import { UserService } from './user.service';

describe('UserResolver', () => {
  let resolver: UserResolver;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [UserResolver, UserService],
    }).compile();

    resolver = module.get<UserResolver>(UserResolver);
  });

  it('should be defined', () => {
    expect(resolver).toBeDefined();
  });
});


