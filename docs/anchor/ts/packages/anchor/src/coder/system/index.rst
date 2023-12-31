ts/packages/anchor/src/coder/system/index.ts
============================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl } from "../../idl.js";
import { Coder } from "../index.js";
import { SystemInstructionCoder } from "./instruction.js";
import { SystemStateCoder } from "./state.js";
import { SystemAccountsCoder } from "./accounts.js";
import { SystemEventsCoder } from "./events.js";
import { SystemTypesCoder } from "./types.js";

/**
 * Coder for the System program.
 */
export class SystemCoder implements Coder {
  readonly instruction: SystemInstructionCoder;
  readonly accounts: SystemAccountsCoder;
  readonly state: SystemStateCoder;
  readonly events: SystemEventsCoder;
  readonly types: SystemTypesCoder;

  constructor(idl: Idl) {
    this.instruction = new SystemInstructionCoder(idl);
    this.accounts = new SystemAccountsCoder(idl);
    this.events = new SystemEventsCoder(idl);
    this.state = new SystemStateCoder(idl);
    this.types = new SystemTypesCoder(idl);
  }
}


