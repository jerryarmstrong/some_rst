src/realm-hub/dto/RealmHubInfoResource.ts
=========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, ObjectType } from '@nestjs/graphql';

import { RichTextDocumentScalar } from '@src/lib/scalars/RichTextDocument';
import { RichTextDocument } from '@src/lib/types/RichTextDocument';

@ObjectType({
  description: 'An external resource relevant to the Realm',
})
export class RealmHubInfoResource {
  @Field({
    description: 'A label for the resouce',
  })
  title: string;

  @Field(() => RichTextDocumentScalar, {
    description: 'Optional body for the resource',
    nullable: true,
  })
  content?: RichTextDocument;

  @Field({
    description: 'Where the resource can be found',
  })
  url: string;
}


