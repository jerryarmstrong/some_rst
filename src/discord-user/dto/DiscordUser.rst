src/discord-user/dto/DiscordUser.ts
===================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, Field } from '@nestjs/graphql';
import { PublicKey } from '@solana/web3.js';

import { PublicKeyScalar } from '@src/lib/scalars/PublicKey';

@ObjectType({
  description: 'A Discord user',
})
export class DiscordUser {
  @Field(() => PublicKeyScalar, { description: 'Public key' })
  publicKey: PublicKey;
}

@ObjectType({
  description: "A Discord user's refresh token",
})
export class RefreshToken {
  @Field({ description: 'Discord user refresh token' })
  token: string;
}


