ts/packages/spl-token/src/coder/index.ts
========================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl, Coder } from "@project-serum/anchor";

import { SplTokenAccountsCoder } from "./accounts";
import { SplTokenEventsCoder } from "./events";
import { SplTokenInstructionCoder } from "./instructions";
import { SplTokenStateCoder } from "./state";
import { SplTokenTypesCoder } from "./types";

/**
 * Coder for SplToken
 */
export class SplTokenCoder implements Coder {
  readonly accounts: SplTokenAccountsCoder;
  readonly events: SplTokenEventsCoder;
  readonly instruction: SplTokenInstructionCoder;
  readonly state: SplTokenStateCoder;
  readonly types: SplTokenTypesCoder;

  constructor(idl: Idl) {
    this.accounts = new SplTokenAccountsCoder(idl);
    this.events = new SplTokenEventsCoder(idl);
    this.instruction = new SplTokenInstructionCoder(idl);
    this.state = new SplTokenStateCoder(idl);
    this.types = new SplTokenTypesCoder(idl);
  }
}


