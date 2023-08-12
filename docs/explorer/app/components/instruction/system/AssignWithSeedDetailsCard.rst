app/components/instruction/system/AssignWithSeedDetailsCard.tsx
===============================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { Copyable } from '@components/common/Copyable';
import { ParsedInstruction, SignatureResult, SystemProgram } from '@solana/web3.js';
import React from 'react';

import { InstructionCard } from '../InstructionCard';
import { AssignWithSeedInfo } from './types';

export function AssignWithSeedDetailsCard(props: {
    ix: ParsedInstruction;
    index: number;
    result: SignatureResult;
    info: AssignWithSeedInfo;
    innerCards?: JSX.Element[];
    childIndex?: number;
}) {
    const { ix, index, result, info, innerCards, childIndex } = props;

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title="System Program: Assign Account w/ Seed"
            innerCards={innerCards}
            childIndex={childIndex}
        >
            <tr>
                <td>Program</td>
                <td className="text-lg-end">
                    <Address pubkey={SystemProgram.programId} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Account Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.account} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Base Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.base} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Seed</td>
                <td className="text-lg-end">
                    <Copyable text={info.seed}>
                        <code>{info.seed}</code>
                    </Copyable>
                </td>
            </tr>

            <tr>
                <td>Assigned Program Id</td>
                <td className="text-lg-end">
                    <Address pubkey={info.owner} alignRight link />
                </td>
            </tr>
        </InstructionCard>
    );
}


