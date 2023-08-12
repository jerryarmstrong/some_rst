ts/packages/spl-associated-token-account/src/coder/state.ts
===========================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl, StateCoder } from "@project-serum/anchor";

export class SplAssociatedTokenAccountStateCoder implements StateCoder {
  constructor(_idl: Idl) {}

  encode<T = any>(_name: string, _account: T): Promise<Buffer> {
    throw new Error("SplAssociatedTokenAccount does not have state");
  }
  decode<T = any>(_ix: Buffer): T {
    throw new Error("SplAssociatedTokenAccount does not have state");
  }
}


