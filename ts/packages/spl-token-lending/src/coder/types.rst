ts/packages/spl-token-lending/src/coder/types.ts
================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl, TypesCoder } from "@project-serum/anchor";

export class SplTokenLendingTypesCoder implements TypesCoder {
  constructor(_idl: Idl) {}

  encode<T = any>(_name: string, _type: T): Buffer {
    throw new Error("SplTokenLending does not have user-defined types");
  }
  decode<T = any>(_name: string, _typeData: Buffer): T {
    throw new Error("SplTokenLending does not have user-defined types");
  }
}


