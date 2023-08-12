packages/sdk/src/generated/index.ts
===================================

Last edited: 2023-04-22 23:05:55

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
export * from './accounts';
export * from './errors';
export * from './instructions';
export * from './types';

/**
 * Program address
 *
 * @category constants
 * @category generated
 */
export const PROGRAM_ADDRESS = 'MyProgram1111111111111111111111111111111111';

/**
 * Program public key
 *
 * @category constants
 * @category generated
 */
export const PROGRAM_ID = new PublicKey(PROGRAM_ADDRESS);


