src/realm/inputDto/RealmFaqItemInput.ts
=======================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, InputType } from '@nestjs/graphql';

import { RichTextDocumentScalar } from '@src/lib/scalars/RichTextDocument';
import { RichTextDocument } from '@src/lib/types/RichTextDocument';

@InputType({
  description: 'A single FAQ item in the Realm Hub',
})
export class RealmFaqItemInput {
  @Field(() => RichTextDocumentScalar, {
    description: 'The answer to a FAQ item question',
  })
  answer: RichTextDocument;

  @Field({
    description: 'The question being asked in the FAQ item',
  })
  question: string;
}


