actions/dryRunInstruction.ts
============================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { InstructionData } from '@solana/spl-governance'

import {
  ComputeBudgetProgram,
  Connection,
  Transaction,
  TransactionInstruction,
} from '@solana/web3.js'
import { WalletAdapter } from '@solana/wallet-adapter-base'

export async function dryRunInstruction(
  connection: Connection,
  wallet: WalletAdapter,
  instructionData: InstructionData | null,
  prerequisiteInstructionsToRun?: TransactionInstruction[] | undefined,
  additionalInstructions?: InstructionData[]
) {
  const transaction = new Transaction({ feePayer: wallet.publicKey })

  transaction.add(
    ComputeBudgetProgram.setComputeUnitLimit({ units: 1_000_000 })
  )

  if (prerequisiteInstructionsToRun) {
    prerequisiteInstructionsToRun.map((x) => transaction.add(x))
  }
  if (additionalInstructions) {
    for (const i of additionalInstructions) {
      transaction.add({
        keys: i.accounts,
        programId: i.programId,
        data: Buffer.from(i.data),
      })
    }
  }

  if (instructionData) {
    transaction.add({
      keys: instructionData.accounts,
      programId: instructionData.programId,
      data: Buffer.from(instructionData.data),
    })
  }

  const result = await connection.simulateTransaction(
    transaction,
    undefined,
    true
  )

  return { response: result.value, transaction }
}


