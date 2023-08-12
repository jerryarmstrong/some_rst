src/realm/inputDto/RealmTokenDetailsInput.ts
============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, InputType } from '@nestjs/graphql';
import { PublicKey } from '@solana/web3.js';

import { PublicKeyScalar } from '@src/lib/scalars/PublicKey';

@InputType({
  description: 'An associated token',
})
export class RealmTokenDetailsInput {
  @Field(() => PublicKeyScalar, {
    description: 'The Mint',
  })
  mint: PublicKey;
}


