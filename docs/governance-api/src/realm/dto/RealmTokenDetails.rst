src/realm/dto/RealmTokenDetails.ts
==================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, ObjectType } from '@nestjs/graphql';
import { PublicKey } from '@solana/web3.js';

import { PublicKeyScalar } from '@src/lib/scalars/PublicKey';

@ObjectType({
  description: 'An associated token',
})
export class RealmTokenDetails {
  @Field(() => PublicKeyScalar, {
    description: 'The Mint',
  })
  mint: PublicKey;
}


