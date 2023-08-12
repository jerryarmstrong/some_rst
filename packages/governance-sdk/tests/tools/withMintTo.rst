packages/governance-sdk/tests/tools/withMintTo.ts
=================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    import { Token, u64 } from '@solana/spl-token'
import { PublicKey, TransactionInstruction } from '@solana/web3.js'
import { TOKEN_PROGRAM_ID } from '../../src/tools/sdk/splToken'



export const withMintTo = async (
  instructions: TransactionInstruction[],
  mintPk: PublicKey,
  destinationPk: PublicKey,
  mintAuthorityPk: PublicKey,
  amount: number | u64
) => {
  instructions.push(
    Token.createMintToInstruction(
      TOKEN_PROGRAM_ID,
      mintPk,
      destinationPk,
      mintAuthorityPk,
      [],
      amount
    )
  )
}


