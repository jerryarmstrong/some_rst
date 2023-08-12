src/discover-page/inputDto/DiscoverPageSpotlightItemStatInput.ts
================================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { InputType, Field } from '@nestjs/graphql';

@InputType({
  description: 'Discover page spotlight item',
})
export class DiscoverPageSpotlightItemStatInput {
  @Field({
    description: 'The value to display for the stat',
  })
  value: string;

  @Field({
    description: 'A label for the stat',
  })
  label: string;
}


