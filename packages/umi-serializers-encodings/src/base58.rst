packages/umi-serializers-encodings/src/base58.ts
================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import type { Serializer } from '@metaplex-foundation/umi-serializers-core';
import { baseX } from './baseX';

/**
 * A string serializer that uses base58 encoding.
 * @category Serializers
 */
export const base58: Serializer<string> = baseX(
  '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
);


