src/idl/IdlAccount.ts
=====================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import type { IdlTypeLeaf, IdlTypeStruct } from './IdlType';

export type IdlAccount = {
  name: string;
  type: IdlTypeStruct;
  docs?: string[];
  seeds?: IdlAccountSeed[];
  size?: number;
};

export type IdlAccountSeed =
  | { kind: 'programId' }
  | { kind: 'constant'; type: IdlTypeLeaf; value: string | boolean | number }
  | { kind: 'variable'; name: string; description: string; type: IdlTypeLeaf };


