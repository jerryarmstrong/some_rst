token/js/src/instructions/initializeNonTransferableMint.ts
==========================================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import { struct, u8 } from '@solana/buffer-layout';
import { PublicKey, TransactionInstruction } from '@solana/web3.js';
import { TokenInstruction } from './types';
import { TokenUnsupportedInstructionError } from '../errors';
import { programSupportsExtensions } from '../constants';

/** Deserialized instruction for the initiation of an immutable owner account */
export interface InitializeNonTransferableMintInstructionData {
    instruction: TokenInstruction.InitializeNonTransferableMint;
}

/** The struct that represents the instruction data as it is read by the program */
export const initializeNonTransferableMintInstructionData = struct<InitializeNonTransferableMintInstructionData>([
    u8('instruction'),
]);

/**
 * Construct an InitializeNonTransferableMint instruction
 *
 * @param mint           Mint Account to make non-transferable
 * @param programId         SPL Token program account
 *
 * @return Instruction to add to a transaction
 */
export function createInitializeNonTransferableMintInstruction(
    mint: PublicKey,
    programId: PublicKey
): TransactionInstruction {
    if (!programSupportsExtensions(programId)) {
        throw new TokenUnsupportedInstructionError();
    }
    const keys = [{ pubkey: mint, isSigner: false, isWritable: true }];

    const data = Buffer.alloc(initializeNonTransferableMintInstructionData.span);
    initializeNonTransferableMintInstructionData.encode(
        {
            instruction: TokenInstruction.InitializeNonTransferableMint,
        },
        data
    );

    return new TransactionInstruction({ keys, programId, data });
}


