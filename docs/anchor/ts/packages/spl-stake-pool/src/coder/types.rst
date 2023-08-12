ts/packages/spl-stake-pool/src/coder/types.ts
=============================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl, TypesCoder } from "@project-serum/anchor";

export class SplStakePoolTypesCoder implements TypesCoder {
  constructor(_idl: Idl) {}

  encode<T = any>(_name: string, _type: T): Buffer {
    throw new Error("SplStakePool does not have user-defined types");
  }
  decode<T = any>(_name: string, _typeData: Buffer): T {
    throw new Error("SplStakePool does not have user-defined types");
  }
}


