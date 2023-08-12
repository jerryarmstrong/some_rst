token/js/src/instructions/createNativeMint.ts
=============================================

Last edited: 2022-07-07 18:10:20

Contents:

.. code-block:: ts

    import { struct, u8 } from '@solana/buffer-layout';
import { PublicKey, TransactionInstruction, SystemProgram } from '@solana/web3.js';
import { TOKEN_2022_PROGRAM_ID, NATIVE_MINT_2022 } from '../constants';
import { TokenInstruction } from './types';
import { TokenUnsupportedInstructionError } from '../errors';
import { programSupportsExtensions } from '../constants';

/** TODO: docs */
export interface CreateNativeMintInstructionData {
    instruction: TokenInstruction.CreateNativeMint;
}

/** TODO: docs */
export const createNativeMintInstructionData = struct<CreateNativeMintInstructionData>([u8('instruction')]);

/**
 * Construct a CreateNativeMint instruction
 *
 * @param account   New token account
 * @param mint      Mint account
 * @param owner     Owner of the new account
 * @param programId SPL Token program account
 *
 * @return Instruction to add to a transaction
 */
export function createCreateNativeMintInstruction(
    payer: PublicKey,
    nativeMintId = NATIVE_MINT_2022,
    programId = TOKEN_2022_PROGRAM_ID
): TransactionInstruction {
    if (!programSupportsExtensions(programId)) {
        throw new TokenUnsupportedInstructionError();
    }
    const keys = [
        { pubkey: payer, isSigner: true, isWritable: true },
        { pubkey: nativeMintId, isSigner: false, isWritable: true },
        { pubkey: SystemProgram.programId, isSigner: false, isWritable: false },
    ];

    const data = Buffer.alloc(createNativeMintInstructionData.span);
    createNativeMintInstructionData.encode({ instruction: TokenInstruction.CreateNativeMint }, data);

    return new TransactionInstruction({ keys, programId, data });
}


