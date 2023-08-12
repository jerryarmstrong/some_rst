app/core/program-plugin/types.ts
================================

Last edited: 2020-09-01 18:17:54

Contents:

.. code-block:: ts

    import { Connection, PublicKey, TransactionInstruction } from "@solana/web3.js"
import { DecodedInstruction, Markdown, Token } from "../types"

export interface PluginContext {
  getConnection: () => Connection
  getSPLToken: (publicKey: PublicKey, connection: Connection) => Promise<Token | undefined>
}

export interface ProgramPlugin {
  // Decode the given instruction into its details elements. If the decoder is unable to decode the
  // given instruction either due to a malformed message or to an unexpected error when querying some
  // state, it should throw an `Error`.
  decode(instruction: TransactionInstruction): DecodedInstruction

  // Enhances a decoded instruction. You may wish to perform third party calls to get more information
  // regarding the transaction, for example you may want to fetch the mint information.
  decorate(
    decodedInstruction: DecodedInstruction,
    context: PluginContext
  ): Promise<DecodedInstruction>

  getMarkdown(decodedInstruction: DecodedInstruction): Markdown

  getRicardian(decodedInstruction: DecodedInstruction): Markdown
}


