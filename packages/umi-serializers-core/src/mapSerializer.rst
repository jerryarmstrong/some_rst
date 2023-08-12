packages/umi-serializers-core/src/mapSerializer.ts
==================================================

Last edited: 2023-07-27 15:49:41

Contents:

.. code-block:: ts

    import { Serializer } from './common';

/**
 * Converts a serializer A to a serializer B by mapping their values.
 * @category Serializers
 */
export function mapSerializer<NewFrom, OldFrom, To extends NewFrom & OldFrom>(
  serializer: Serializer<OldFrom, To>,
  unmap: (value: NewFrom) => OldFrom
): Serializer<NewFrom, To>;
export function mapSerializer<
  NewFrom,
  OldFrom,
  NewTo extends NewFrom = NewFrom,
  OldTo extends OldFrom = OldFrom
>(
  serializer: Serializer<OldFrom, OldTo>,
  unmap: (value: NewFrom) => OldFrom,
  map: (value: OldTo, buffer: Uint8Array, offset: number) => NewTo
): Serializer<NewFrom, NewTo>;
export function mapSerializer<
  NewFrom,
  OldFrom,
  NewTo extends NewFrom = NewFrom,
  OldTo extends OldFrom = OldFrom
>(
  serializer: Serializer<OldFrom, OldTo>,
  unmap: (value: NewFrom) => OldFrom,
  map?: (value: OldTo, buffer: Uint8Array, offset: number) => NewTo
): Serializer<NewFrom, NewTo> {
  return {
    description: serializer.description,
    fixedSize: serializer.fixedSize,
    maxSize: serializer.maxSize,
    serialize: (value: NewFrom) => serializer.serialize(unmap(value)),
    deserialize: (buffer: Uint8Array, offset = 0) => {
      const [value, length] = serializer.deserialize(buffer, offset);
      return map
        ? [map(value, buffer, offset), length]
        : [value as any, length];
    },
  };
}


