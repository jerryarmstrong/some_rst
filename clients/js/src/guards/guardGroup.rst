clients/js/src/guards/guardGroup.ts
===================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import {
  mapSerializer,
  Serializer,
  string,
  struct,
} from '@metaplex-foundation/umi/serializers';
import { GuardGroupLabelTooLongError } from '../errors';
import { CANDY_GUARD_LABEL_SIZE } from '../constants';
import { CandyGuardProgram, GuardRepository } from './guardRepository';
import { getGuardSetSerializer, GuardSet, GuardSetArgs } from './guardSet';

/**
 * A group represent a specific set of guards. When groups are used, transactions
 * must specify which group should be used during validation.
 */
export type GuardGroup<D extends GuardSet> = {
  label: string;
  guards: D;
};

export type GuardGroupArgs<DA extends GuardSetArgs> = {
  label: string;
  guards: Partial<DA>;
};

export function getGuardGroupSerializer<
  DA extends GuardSetArgs,
  D extends DA & GuardSet
>(
  context: { guards: GuardRepository },
  program: CandyGuardProgram
): Serializer<GuardGroupArgs<DA>, GuardGroup<D>> {
  return struct(
    [
      [
        'label',
        mapSerializer(
          string({ size: CANDY_GUARD_LABEL_SIZE }),
          (label: string): string => {
            if (label.length > CANDY_GUARD_LABEL_SIZE) {
              throw new GuardGroupLabelTooLongError(label);
            }
            return label;
          }
        ),
      ],
      ['guards', getGuardSetSerializer<DA, D>(context, program)],
    ],
    { description: 'GuardGroup' }
  ) as Serializer<GuardGroupArgs<DA>, GuardGroup<D>>;
}


