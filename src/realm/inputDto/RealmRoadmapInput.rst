src/realm/inputDto/RealmRoadmapInput.ts
=======================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, InputType } from '@nestjs/graphql';

import { RichTextDocumentScalar } from '@src/lib/scalars/RichTextDocument';
import { RichTextDocument } from '@src/lib/types/RichTextDocument';

import { RealmRoadmapItemInput } from './RealmRoadmapItemInput';

@InputType({
  description: 'The roadmap for a Realm',
})
export class RealmRoadmapInput {
  @Field(() => RichTextDocumentScalar, {
    description: 'An optional description for the roadmap',
    nullable: true,
  })
  description?: RichTextDocument;

  @Field(() => [RealmRoadmapItemInput], {
    description: 'The items on the roadmap',
  })
  items: RealmRoadmapItemInput[];
}


