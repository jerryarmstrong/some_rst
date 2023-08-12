src/user/dto/User.ts
====================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, Field } from '@nestjs/graphql';
import { PublicKey } from '@solana/web3.js';

import { PublicKeyScalar } from '@src/lib/scalars/PublicKey';

@ObjectType({
  description: 'A user',
})
export class User {
  @Field(() => PublicKeyScalar, { description: "User's public key" })
  publicKey: PublicKey;
}


