src/realm-treasury/dto/RealmTreasury.ts
=======================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, ObjectType } from '@nestjs/graphql';
import { PublicKey } from '@solana/web3.js';

import { PublicKeyScalar } from '@lib/scalars/PublicKey';

@ObjectType({
  description: "A realm's treasury",
})
export class RealmTreasury {
  @Field(() => PublicKeyScalar, {
    description: 'The realm the treasury belongs to',
  })
  belongsTo: PublicKey;
}


