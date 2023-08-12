packages/sdk/core/src/utils/borsh/deserialize.ts
================================================

Last edited: 2022-07-15 16:27:40

Contents:

.. code-block:: ts

    import { Schema, BinaryReader } from 'borsh';

import { deserializeStruct } from './deserializeStruct';

export function deserialize(schema: Schema, classType: any, buffer: Buffer): any {
  const reader = new BinaryReader(buffer);
  return deserializeStruct(schema, classType, reader);
}


