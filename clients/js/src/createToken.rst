clients/js/src/createToken.ts
=============================

Last edited: 2023-06-19 17:40:55

Contents:

.. code-block:: ts

    import {
  Context,
  PublicKey,
  Signer,
  transactionBuilder,
  TransactionBuilder,
} from '@metaplex-foundation/umi';
import {
  createAccountWithRent,
  getTokenSize,
  initializeToken3,
} from './generated';

// Inputs.
export type CreateTokenArgs = {
  token: Signer;
  mint: PublicKey;
  owner?: PublicKey;
};

// Instruction.
export function createToken(
  context: Pick<Context, 'programs' | 'identity' | 'payer'>,
  input: CreateTokenArgs
): TransactionBuilder {
  return transactionBuilder()
    .add(
      createAccountWithRent(context, {
        newAccount: input.token,
        space: getTokenSize(),
        programId: context.programs.get('splToken').publicKey,
      })
    )
    .add(
      initializeToken3(context, {
        account: input.token.publicKey,
        mint: input.mint,
        owner: input.owner ?? context.identity.publicKey,
      })
    );
}


