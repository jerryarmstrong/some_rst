src/realm/inputDto/RealmAboutSectionInput.ts
============================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { Field, InputType } from '@nestjs/graphql';

import { RichTextDocumentScalar } from '@src/lib/scalars/RichTextDocument';
import { RichTextDocument } from '@src/lib/types/RichTextDocument';

@InputType({
  description: "A single section in a Realm's hub info",
})
export class RealmAboutSectionInput {
  @Field({
    description: 'An optional title for the section',
    nullable: true,
  })
  heading?: string;

  @Field(() => RichTextDocumentScalar, {
    description: 'A rich text document containing the body of the section',
  })
  content: RichTextDocument;
}


