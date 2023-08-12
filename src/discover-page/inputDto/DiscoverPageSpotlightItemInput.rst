src/discover-page/inputDto/DiscoverPageSpotlightItemInput.ts
============================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { InputType, Field } from '@nestjs/graphql';
import { PublicKey } from '@solana/web3.js';

import { PublicKeyScalar } from '@lib/scalars/PublicKey';

import { DiscoverPageSpotlightItemStatInput } from './DiscoverPageSpotlightItemStatInput';

@InputType({
  description: 'Discover page spotlight item',
})
export class DiscoverPageSpotlightItemInput {
  @Field({
    description: 'Hero image for the spotlight',
  })
  heroImageUrl: string;

  @Field({
    description: 'Title',
  })
  title: string;

  @Field(() => PublicKeyScalar, {
    description: 'PublicKey of the realm',
  })
  publicKey: PublicKey;

  @Field({
    description: 'A description for the Spotlight',
  })
  description: string;

  @Field(() => [DiscoverPageSpotlightItemStatInput], {
    description: 'A list of stats to display',
  })
  stats: DiscoverPageSpotlightItemStatInput[];
}


