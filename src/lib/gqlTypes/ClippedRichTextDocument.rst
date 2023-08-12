src/lib/gqlTypes/ClippedRichTextDocument.ts
===========================================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import { ObjectType, Field } from '@nestjs/graphql';

import { RichTextDocumentScalar } from '@lib/scalars/RichTextDocument';
import { RichTextDocument } from '@lib/types/RichTextDocument';

@ObjectType({
  description: 'A rich text document that has been clipped at a given character count',
})
export class ClippedRichTextDocument {
  @Field(() => RichTextDocumentScalar, {
    description: 'The clipped document',
  })
  document: RichTextDocument;

  @Field(() => Boolean, {
    description: 'Indicates whether the document was clipped. If the document is shorter than the given character count, it may not be clipped',
  })
  isClipped: boolean;
}


