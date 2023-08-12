packages/transactions/src/serializers/instruction.ts
====================================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import { array, bytes, mapSerializer, Serializer, shortU16, struct, u8 } from '@metaplex-foundation/umi-serializers';

import { getCompiledInstructions } from '../compile-instructions';

type Instruction = ReturnType<typeof getCompiledInstructions>[number];

export function getInstructionCodec(): Serializer<Instruction> {
    return mapSerializer<Instruction, Required<Instruction>>(
        struct([
            [
                'programAddressIndex',
                u8(
                    __DEV__
                        ? {
                              description:
                                  'The index of the program being called, according to the ' +
                                  'well-ordered accounts list for this transaction',
                          }
                        : undefined
                ),
            ],
            [
                'accountIndices',
                array(
                    u8({
                        description: __DEV__
                            ? 'The index of an account, according to the well-ordered accounts ' +
                              'list for this transaction'
                            : '',
                    }),
                    {
                        description: __DEV__
                            ? 'An optional list of account indices, according to the ' +
                              'well-ordered accounts list for this transaction, in the order in ' +
                              'which the program being called expects them'
                            : '',
                        size: shortU16(),
                    }
                ),
            ],
            [
                'data',
                bytes({
                    description: __DEV__ ? 'An optional buffer of data passed to the instruction' : '',
                    size: shortU16(),
                }),
            ],
        ]),
        (value: Instruction) => {
            if (value.accountIndices !== undefined && value.data !== undefined) {
                return value as Required<Instruction>;
            }
            return {
                ...value,
                accountIndices: value.accountIndices ?? [],
                data: value.data ?? new Uint8Array(0),
            } as Required<Instruction>;
        },
        (value: Required<Instruction>) => {
            if (value.accountIndices.length && value.data.byteLength) {
                return value;
            }
            const { accountIndices, data, ...rest } = value;
            return {
                ...rest,
                ...(accountIndices.length ? { accountIndices } : null),
                ...(data.byteLength ? { data } : null),
            };
        }
    );
}


