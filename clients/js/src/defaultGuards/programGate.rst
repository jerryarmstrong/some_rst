clients/js/src/defaultGuards/programGate.ts
===========================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import {
  fixSerializer,
  mapSerializer,
} from '@metaplex-foundation/umi/serializers';
import { MaximumOfFiveAdditionalProgramsError } from '../errors';
import {
  ProgramGate,
  ProgramGateArgs,
  getProgramGateSerializer,
} from '../generated';
import { GuardManifest, noopParser } from '../guards';

/**
 * The programGate guard restricts the programs that can be invoked within
 * the mint transaction. It allows the necessary programs for the mint
 * instruction to work and any other program specified in the configuration.
 *
 * The `additional` argument allows you to specify additional programs
 * that can be invoked in a mint transaction.
 * These programs are in addition to the mandatory programs that
 * are required for the mint instruction to work. Providing an empty
 * array is equivalent to only authorising the mandatory programs.
 *
 * The mandatory programs are:
 * - The SPL System Program
 * - The SPL Token Program
 * - The SPL Associated Token Program
 * - The SPL Compute Budget Program
 * - The MPL Candy Machine Core Program
 * - The MPL Candy Guard Program
 * - The MPL System Extras Program
 */
export const programGateGuardManifest: GuardManifest<
  ProgramGateArgs,
  ProgramGate
> = {
  name: 'programGate',
  serializer: () =>
    mapSerializer(
      fixSerializer(getProgramGateSerializer(), 4 + 32 * 5),
      (value) => {
        if (value.additional.length > 5) {
          throw new MaximumOfFiveAdditionalProgramsError();
        }
        return value;
      }
    ),
  mintParser: noopParser,
  routeParser: noopParser,
};


