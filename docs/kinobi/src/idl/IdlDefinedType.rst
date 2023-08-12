src/idl/IdlDefinedType.ts
=========================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import type { IdlTypeEnum, IdlTypeStruct } from './IdlType';

export type IdlDefinedType = {
  name: string;
  type: IdlTypeStruct | IdlTypeEnum;
  docs?: string[];
};


