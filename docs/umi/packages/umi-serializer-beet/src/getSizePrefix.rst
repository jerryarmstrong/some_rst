packages/umi-serializer-beet/src/getSizePrefix.ts
=================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { ArrayLikeSerializerSize } from '@metaplex-foundation/umi';

export function getSizePrefix(
  size: ArrayLikeSerializerSize,
  realSize: number
): Uint8Array {
  return typeof size === 'object' ? size.serialize(realSize) : new Uint8Array();
}


