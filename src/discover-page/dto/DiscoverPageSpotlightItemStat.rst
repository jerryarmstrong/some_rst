src/discover-page/dto/DiscoverPageSpotlightItemStat.ts
======================================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, Field } from '@nestjs/graphql';

@ObjectType({
  description: 'Discover page spotlight item',
})
export class DiscoverPageSpotlightItemStat {
  @Field({
    description: 'The value to display for the stat',
  })
  value: string;

  @Field({
    description: 'A label for the stat',
  })
  label: string;
}


