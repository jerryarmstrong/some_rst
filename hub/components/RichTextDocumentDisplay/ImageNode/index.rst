hub/components/RichTextDocumentDisplay/ImageNode/index.tsx
==========================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import { ImageNode as ImageNodeModel } from '@hub/types/RichTextDocument';

interface Props {
  className?: string;
  image: ImageNodeModel;
  isClipped?: boolean;
  isLast?: boolean;
  showExpand?: boolean;
  onExpand?(): void;
}

// eslint-disable-next-line
export function ImageNode(props: Props) {
  return <div />;
}


