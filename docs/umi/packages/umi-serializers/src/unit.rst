packages/umi-serializers/src/unit.ts
====================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import {
  BaseSerializerOptions,
  Serializer,
} from '@metaplex-foundation/umi-serializers-core';

/**
 * Defines the options for unit serializers.
 * @category Serializers
 */
export type UnitSerializerOptions = BaseSerializerOptions;

/**
 * Creates a void serializer.
 *
 * @param options - A set of options for the serializer.
 */
export function unit(options: UnitSerializerOptions = {}): Serializer<void> {
  return {
    description: options.description ?? 'unit',
    fixedSize: 0,
    maxSize: 0,
    serialize: () => new Uint8Array(),
    deserialize: (_bytes: Uint8Array, offset = 0) => [undefined, offset],
  };
}


