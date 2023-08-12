src/idl/Idl.ts
==============

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import type { IdlAccount } from './IdlAccount';
import type { IdlDefinedType } from './IdlDefinedType';
import type { IdlError } from './IdlError';
import type { IdlInstruction } from './IdlInstruction';

export type Idl = {
  version: string;
  name: string;
  instructions: IdlInstruction[];
  accounts?: IdlAccount[];
  errors?: IdlError[];
  types?: IdlDefinedType[];
  metadata: {
    address: string;
    origin?: 'anchor' | 'shank';
    binaryVersion?: string;
    libVersion?: string;
  };
};


