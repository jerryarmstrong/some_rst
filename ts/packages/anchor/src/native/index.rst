ts/packages/anchor/src/native/index.ts
======================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Program, Provider } from "../index.js";
import { program as systemProgram, SystemProgram } from "./system.js";

export { SystemProgram } from "./system.js";

export class Native {
  public static system(provider?: Provider): Program<SystemProgram> {
    return systemProgram(provider);
  }
}


