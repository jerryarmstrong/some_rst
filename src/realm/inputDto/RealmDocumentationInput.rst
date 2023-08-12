src/realm/inputDto/RealmDocumentationInput.ts
=============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, InputType } from '@nestjs/graphql';

@InputType({
  description: 'Documentation for the Realm',
})
export class RealmDocumentationInput {
  @Field({
    description: 'A label for the documentation',
    nullable: true,
  })
  title?: string;

  @Field({
    description: 'Where the documentation can be found',
  })
  url: string;
}


