ts/packages/spl-stateless-asks/src/coder/types.ts
=================================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Idl, TypesCoder } from "@project-serum/anchor";

export class SplStatelessAsksTypesCoder implements TypesCoder {
  constructor(_idl: Idl) {}

  encode<T = any>(_name: string, _type: T): Buffer {
    throw new Error("SplStatelessAsks does not have user-defined types");
  }
  decode<T = any>(_name: string, _typeData: Buffer): T {
    throw new Error("SplStatelessAsks does not have user-defined types");
  }
}


