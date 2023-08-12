packages/umi-serializer-beet/src/getSizeDescription.ts
======================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { ArrayLikeSerializerSize } from '@metaplex-foundation/umi';

export function getSizeDescription(
  size: ArrayLikeSerializerSize | string
): string {
  return typeof size === 'object' ? size.description : `${size}`;
}


