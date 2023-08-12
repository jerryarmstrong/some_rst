packages/umi-serializer-data-view/src/plugin.ts
===============================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { UmiPlugin } from '@metaplex-foundation/umi';
import {
  DataViewSerializerOptions,
  createDataViewSerializer,
} from './createDataViewSerializer';

export const dataViewSerializer = (
  options: DataViewSerializerOptions = {}
): UmiPlugin => ({
  install(umi) {
    umi.serializer = createDataViewSerializer(options);
  },
});


