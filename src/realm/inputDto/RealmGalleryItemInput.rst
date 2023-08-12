src/realm/inputDto/RealmGalleryItemInput.ts
===========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, InputType } from '@nestjs/graphql';

@InputType({
  description: 'An item in the gallery',
})
export class RealmGalleryItemInput {
  @Field({
    description: 'An optional caption for the item',
    nullable: true,
  })
  caption: string;

  @Field({
    description: 'The height of the item',
  })
  height: number;

  @Field({
    description: 'The width of the item',
  })
  width: number;

  @Field({
    description: 'A url for the item',
  })
  url: string;
}


