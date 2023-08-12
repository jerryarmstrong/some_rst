src/realm-member/dto/RealmMember.ts
===================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, Field } from '@nestjs/graphql';
import { PublicKey } from '@solana/web3.js';

import { PublicKeyScalar } from '@src/lib/scalars/PublicKey';

@ObjectType({
  description: 'A member of a Realm',
})
export class RealmMember {
  @Field(() => PublicKeyScalar, {
    description: 'Public Key address for the Realm Member',
  })
  publicKey: PublicKey;
}


