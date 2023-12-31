ts/packages/anchor/src/coder/borsh/index.ts
===========================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl } from "../../idl.js";
import { BorshInstructionCoder } from "./instruction.js";
import { BorshAccountsCoder } from "./accounts.js";
import { BorshEventCoder } from "./event.js";
import { BorshStateCoder } from "./state.js";
import { BorshTypesCoder } from "./types.js";
import { Coder } from "../index.js";

export { BorshInstructionCoder } from "./instruction.js";
export { BorshAccountsCoder, ACCOUNT_DISCRIMINATOR_SIZE } from "./accounts.js";
export { BorshEventCoder, eventDiscriminator } from "./event.js";
export { BorshStateCoder, stateDiscriminator } from "./state.js";

/**
 * BorshCoder is the default Coder for Anchor programs implementing the
 * borsh based serialization interface.
 */
export class BorshCoder<A extends string = string, T extends string = string>
  implements Coder
{
  /**
   * Instruction coder.
   */
  readonly instruction: BorshInstructionCoder;

  /**
   * Account coder.
   */
  readonly accounts: BorshAccountsCoder<A>;

  /**
   * Coder for state structs.
   */
  readonly state: BorshStateCoder;

  /**
   * Coder for events.
   */
  readonly events: BorshEventCoder;

  /**
   * Coder for user-defined types.
   */
  readonly types: BorshTypesCoder<T>;

  constructor(idl: Idl) {
    this.instruction = new BorshInstructionCoder(idl);
    this.accounts = new BorshAccountsCoder(idl);
    this.events = new BorshEventCoder(idl);
    if (idl.state) {
      this.state = new BorshStateCoder(idl);
    }
    this.types = new BorshTypesCoder(idl);
  }
}


