packages/js/src/plugins/tokenModule/program.ts
==============================================

Last edited: 2023-05-26 09:49:40

Contents:

.. code-block:: ts

    import {
  ASSOCIATED_TOKEN_PROGRAM_ID,
  TOKEN_PROGRAM_ID,
} from '@solana/spl-token';
import { Program } from '@/types';

/** @group Programs */
export const tokenProgram: Program = {
  name: 'TokenProgram',
  address: TOKEN_PROGRAM_ID,
};

/** @group Programs */
export const associatedTokenProgram: Program = {
  name: 'AssociatedTokenProgram',
  address: ASSOCIATED_TOKEN_PROGRAM_ID,
};


