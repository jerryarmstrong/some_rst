src/realm/dto/RealmRoadmap.ts
=============================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, ObjectType } from '@nestjs/graphql';

import { RichTextDocumentScalar } from '@src/lib/scalars/RichTextDocument';
import { RichTextDocument } from '@src/lib/types/RichTextDocument';

import { RealmRoadmapItem } from './RealmRoadmapItem';

@ObjectType({
  description: 'The roadmap for a Realm',
})
export class RealmRoadmap {
  @Field(() => RichTextDocumentScalar, {
    description: 'An optional description for the roadmap',
    nullable: true,
  })
  description?: RichTextDocument;

  @Field(() => [RealmRoadmapItem], {
    description: 'The items on the roadmap',
  })
  items: RealmRoadmapItem[];
}


