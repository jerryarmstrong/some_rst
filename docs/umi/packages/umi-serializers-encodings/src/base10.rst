packages/umi-serializers-encodings/src/base10.ts
================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import type { Serializer } from '@metaplex-foundation/umi-serializers-core';
import { baseX } from './baseX';

/**
 * A string serializer that uses base10 encoding.
 * @category Serializers
 */
export const base10: Serializer<string> = baseX('0123456789');


