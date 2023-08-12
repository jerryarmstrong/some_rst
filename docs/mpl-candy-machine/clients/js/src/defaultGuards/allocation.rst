clients/js/src/defaultGuards/allocation.ts
==========================================

Last edited: 2023-08-11 23:25:39

Contents:

.. code-block:: ts

    import { getSplSystemProgramId } from '@metaplex-foundation/mpl-toolbox';
import { Signer } from '@metaplex-foundation/umi';
import {
  findAllocationTrackerPda,
  getAllocationSerializer,
  Allocation,
  AllocationArgs,
} from '../generated';
import { GuardManifest } from '../guards';

/**
 * Guard to specify the maximum number of mints in a guard set.
 *
 */
export const allocationGuardManifest: GuardManifest<
  AllocationArgs,
  Allocation,
  AllocationMintArgs,
  AllocationRouteArgs
> = {
  name: 'allocation',
  serializer: getAllocationSerializer,
  mintParser: (context, mintContext, args) => ({
    data: new Uint8Array(),
    remainingAccounts: [
      {
        publicKey: findAllocationTrackerPda(context, {
          id: args.id,
          candyMachine: mintContext.candyMachine,
          candyGuard: mintContext.candyGuard,
        })[0],
        isWritable: true,
      },
    ],
  }),
  routeParser: (context, routeContext, args) => ({
    data: new Uint8Array(),
    remainingAccounts: [
      {
        isWritable: true,
        publicKey: findAllocationTrackerPda(context, {
          id: args.id,
          candyMachine: routeContext.candyMachine,
          candyGuard: routeContext.candyGuard,
        })[0],
      },
      { isWritable: false, signer: args.candyGuardAuthority },
      { isWritable: false, publicKey: getSplSystemProgramId(context) },
    ],
  }),
};

export type AllocationMintArgs = Omit<AllocationArgs, 'limit'>;

/**
 * The allocation guard arguments that should be provided
 * when accessing the guard's special "route" instruction.
 */
export type AllocationRouteArgs = Omit<AllocationArgs, 'limit'> & {
  /** The authority of the Candy Guard as a Signer. */
  candyGuardAuthority: Signer;
};


