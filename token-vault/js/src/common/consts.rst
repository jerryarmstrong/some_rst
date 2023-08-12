token-vault/js/src/common/consts.ts
===================================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js';
import { PROGRAM_ADDRESS, PROGRAM_ID } from '../generated';

const WRAPPED_SOL_MINT = new PublicKey('So11111111111111111111111111111111111111112');
export const QUOTE_MINT = WRAPPED_SOL_MINT;

// TODO(thlorenz): shank parse out of Rust
export const VAULT_PREFIX = 'vault';
export const VAULT_PROGRAM_ADDRESS = PROGRAM_ADDRESS;
export const VAULT_PROGRAM_ID = PROGRAM_ID;


