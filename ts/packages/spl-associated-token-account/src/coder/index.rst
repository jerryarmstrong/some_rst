ts/packages/spl-associated-token-account/src/coder/index.ts
===========================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl, Coder } from "@project-serum/anchor";

import { SplAssociatedTokenAccountAccountsCoder } from "./accounts";
import { SplAssociatedTokenAccountEventsCoder } from "./events";
import { SplAssociatedTokenAccountInstructionCoder } from "./instructions";
import { SplAssociatedTokenAccountStateCoder } from "./state";
import { SplAssociatedTokenAccountTypesCoder } from "./types";

/**
 * Coder for SplAssociatedTokenAccount
 */
export class SplAssociatedTokenAccountCoder implements Coder {
  readonly accounts: SplAssociatedTokenAccountAccountsCoder;
  readonly events: SplAssociatedTokenAccountEventsCoder;
  readonly instruction: SplAssociatedTokenAccountInstructionCoder;
  readonly state: SplAssociatedTokenAccountStateCoder;
  readonly types: SplAssociatedTokenAccountTypesCoder;

  constructor(idl: Idl) {
    this.accounts = new SplAssociatedTokenAccountAccountsCoder(idl);
    this.events = new SplAssociatedTokenAccountEventsCoder(idl);
    this.instruction = new SplAssociatedTokenAccountInstructionCoder(idl);
    this.state = new SplAssociatedTokenAccountStateCoder(idl);
    this.types = new SplAssociatedTokenAccountTypesCoder(idl);
  }
}


