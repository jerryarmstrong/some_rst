src/realm/dto/RealmFaqItem.ts
=============================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, ObjectType } from '@nestjs/graphql';

import { RichTextDocumentScalar } from '@src/lib/scalars/RichTextDocument';
import { RichTextDocument } from '@src/lib/types/RichTextDocument';

@ObjectType({
  description: 'A single FAQ item in the Realm Hub',
})
export class RealmFaqItem {
  @Field(() => RichTextDocumentScalar, {
    description: 'The answer to a FAQ item question',
  })
  answer: RichTextDocument;

  @Field({
    description: 'The question being asked in the FAQ item',
  })
  question: string;
}


