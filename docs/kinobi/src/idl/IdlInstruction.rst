src/idl/IdlInstruction.ts
=========================

Last edited: 2023-08-04 12:58:33

Contents:

.. code-block:: ts

    import type { IdlType } from './IdlType';

export type IdlInstruction = {
  name: string;
  accounts: IdlInstructionAccount[];
  args: IdlInstructionArg[];
  defaultOptionalAccounts?: boolean;
  legacyOptionalAccountsStrategy?: boolean;
  discriminant?: IdlInstructionDiscriminant;
  docs?: string[];
};

export type IdlInstructionAccount = {
  name: string;
  isMut: boolean;
  isSigner: boolean;
  isOptionalSigner?: boolean;
  isOptional?: boolean;
  optional?: boolean;
  docs?: string[];
  desc?: string;
};

export type IdlInstructionArg = {
  name: string;
  type: IdlType;
};

export type IdlInstructionDiscriminant = {
  type: IdlType;
  value: number;
};


