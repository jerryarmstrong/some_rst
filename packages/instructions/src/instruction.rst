packages/instructions/src/instruction.ts
========================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { Base58EncodedAddress } from '@solana/addresses';

import { IAccountLookupMeta, IAccountMeta } from './accounts';

export interface IInstruction<TProgramAddress extends string = string> {
    readonly accounts?: readonly (IAccountMeta | IAccountLookupMeta)[];
    readonly data?: Uint8Array;
    readonly programAddress: Base58EncodedAddress<TProgramAddress>;
}

export interface IInstructionWithAccounts<TAccounts extends readonly (IAccountMeta | IAccountLookupMeta)[]>
    extends IInstruction {
    readonly accounts: TAccounts;
}

export interface IInstructionWithData<TData extends Uint8Array> extends IInstruction {
    readonly data: TData;
}


