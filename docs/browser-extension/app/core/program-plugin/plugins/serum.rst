app/core/program-plugin/plugins/serum.ts
========================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    import { TransactionInstruction } from "@solana/web3.js"
import { createLogger } from "../../utils"
import { DecodedInstruction } from "../../types"
import { INSTRUCTION_LAYOUT } from "@project-serum/serum/lib/instructions"
import { DecoderError } from "../common"

const log = createLogger("sol:decoder:serum")

export class SerumDecoder {
  decodeInstruction = async (instruction: TransactionInstruction): Promise<DecodedInstruction> => {
    console.log("decoding instruction: %O", instruction)
    const foo = INSTRUCTION_LAYOUT.decode(instruction.data)

    log("Decoding serum transaction: %O", foo)

    throw new DecoderError(
      `Serum instruction (from program ${instruction.programId}) are not supported yet`
    )
  }
}


