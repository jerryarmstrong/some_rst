app/components/instruction/stake/MergeDetailsCard.tsx
=====================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { ParsedInstruction, SignatureResult, StakeProgram } from '@solana/web3.js';
import React from 'react';

import { InstructionCard } from '../InstructionCard';
import { MergeInfo } from './types';

export function MergeDetailsCard(props: {
    ix: ParsedInstruction;
    index: number;
    result: SignatureResult;
    info: MergeInfo;
    innerCards?: JSX.Element[];
    childIndex?: number;
}) {
    const { ix, index, result, info, innerCards, childIndex } = props;

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title="Stake Program: Merge Stake"
            innerCards={innerCards}
            childIndex={childIndex}
        >
            <tr>
                <td>Program</td>
                <td className="text-lg-end">
                    <Address pubkey={StakeProgram.programId} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Stake Source</td>
                <td className="text-lg-end">
                    <Address pubkey={info.source} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Stake Destination</td>
                <td className="text-lg-end">
                    <Address pubkey={info.destination} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Authority Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.stakeAuthority} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Clock Sysvar</td>
                <td className="text-lg-end">
                    <Address pubkey={info.clockSysvar} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Stake History Sysvar</td>
                <td className="text-lg-end">
                    <Address pubkey={info.stakeHistorySysvar} alignRight link />
                </td>
            </tr>
        </InstructionCard>
    );
}


