packages/js/src/plugins/candyMachineV2Module/pdas.ts
====================================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import { Buffer } from 'buffer';
import { PublicKey } from '@solana/web3.js';
import { CandyMachineV2Program } from './program';
import { Pda } from '@/types';

/** @group Pdas */
export const findCandyMachineV2CreatorPda = (
  candyMachine: PublicKey,
  programId: PublicKey = CandyMachineV2Program.publicKey
): Pda => {
  return Pda.find(programId, [
    Buffer.from('candy_machine', 'utf8'),
    candyMachine.toBuffer(),
  ]);
};

/** @group Pdas */
export const findCandyMachineV2CollectionPda = (
  candyMachine: PublicKey,
  programId: PublicKey = CandyMachineV2Program.publicKey
): Pda => {
  return Pda.find(programId, [
    Buffer.from('collection', 'utf8'),
    candyMachine.toBuffer(),
  ]);
};


