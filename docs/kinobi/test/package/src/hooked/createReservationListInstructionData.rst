test/package/src/hooked/createReservationListInstructionData.ts
===============================================================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import {
  mapSerializer,
  Serializer,
  struct,
  u8,
} from '@metaplex-foundation/umi/serializers';

export type CreateReservationListInstructionData = { discriminator: number };

export type CreateReservationListInstructionDataArgs = {};

export function getCreateReservationListInstructionDataSerializer(): Serializer<
  CreateReservationListInstructionDataArgs,
  CreateReservationListInstructionData
> {
  return mapSerializer<
    CreateReservationListInstructionDataArgs,
    CreateReservationListInstructionData,
    CreateReservationListInstructionData
  >(
    struct<CreateReservationListInstructionData>([['discriminator', u8()]], {
      description: 'CreateReservationListInstructionData',
    }),
    (value) =>
      ({ ...value, discriminator: 6 } as CreateReservationListInstructionData)
  ) as Serializer<
    CreateReservationListInstructionDataArgs,
    CreateReservationListInstructionData
  >;
}


