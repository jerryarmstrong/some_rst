packages/umi-serializer-beet/src/plugin.ts
==========================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import {
  BeetSerializerOptions,
  createBeetSerializer,
} from './createBeetSerializer';

export const beetSerializer = (
  options: BeetSerializerOptions = {}
): UmiPlugin => ({
  install(umi) {
    umi.serializer = createBeetSerializer(options);
  },
});


