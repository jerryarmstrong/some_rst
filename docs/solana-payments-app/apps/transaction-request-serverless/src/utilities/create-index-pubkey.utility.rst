apps/transaction-request-serverless/src/utilities/create-index-pubkey.utility.ts
================================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import * as web3 from '@solana/web3.js';

export const createIndexPubkey = async (input: string): Promise<web3.PublicKey> => {
    // TODO: There is some max length on what our input string can be, figure it out and validate
    // the constraint here
    return await web3.PublicKey.findProgramAddressSync([Buffer.from(input)], web3.SystemProgram.programId)[0];
};


