ts/packages/spl-binary-oracle-pair/src/coder/index.ts
=====================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl, Coder } from "@project-serum/anchor";

import { SplBinaryOraclePairAccountsCoder } from "./accounts";
import { SplBinaryOraclePairEventsCoder } from "./events";
import { SplBinaryOraclePairInstructionCoder } from "./instructions";
import { SplBinaryOraclePairStateCoder } from "./state";
import { SplBinaryOraclePairTypesCoder } from "./types";

/**
 * Coder for SplBinaryOraclePair
 */
export class SplBinaryOraclePairCoder implements Coder {
  readonly accounts: SplBinaryOraclePairAccountsCoder;
  readonly events: SplBinaryOraclePairEventsCoder;
  readonly instruction: SplBinaryOraclePairInstructionCoder;
  readonly state: SplBinaryOraclePairStateCoder;
  readonly types: SplBinaryOraclePairTypesCoder;

  constructor(idl: Idl) {
    this.accounts = new SplBinaryOraclePairAccountsCoder(idl);
    this.events = new SplBinaryOraclePairEventsCoder(idl);
    this.instruction = new SplBinaryOraclePairInstructionCoder(idl);
    this.state = new SplBinaryOraclePairStateCoder(idl);
    this.types = new SplBinaryOraclePairTypesCoder(idl);
  }
}


