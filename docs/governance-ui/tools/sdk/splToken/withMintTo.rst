tools/sdk/splToken/withMintTo.ts
================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { Token, u64 } from '@solana/spl-token'
import { PublicKey, TransactionInstruction } from '@solana/web3.js'

import { TOKEN_PROGRAM_ID } from '@utils/tokens'

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


