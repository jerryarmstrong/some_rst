app/components/instruction/system/TransferWithSeedDetailsCard.tsx
=================================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { Copyable } from '@components/common/Copyable';
import { SolBalance } from '@components/common/SolBalance';
import { ParsedInstruction, SignatureResult, SystemProgram } from '@solana/web3.js';
import React from 'react';

import { InstructionCard } from '../InstructionCard';
import { TransferWithSeedInfo } from './types';

export function TransferWithSeedDetailsCard(props: {
    ix: ParsedInstruction;
    index: number;
    result: SignatureResult;
    info: TransferWithSeedInfo;
    innerCards?: JSX.Element[];
    childIndex?: number;
}) {
    const { ix, index, result, info, innerCards, childIndex } = props;

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title="System Program: Transfer w/ Seed"
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
                <td>From Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.source} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Destination Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.destination} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Base Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.sourceBase} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Transfer Amount (SOL)</td>
                <td className="text-lg-end">
                    <SolBalance lamports={info.lamports} />
                </td>
            </tr>

            <tr>
                <td>Seed</td>
                <td className="text-lg-end">
                    <Copyable text={info.sourceSeed}>
                        <code>{info.sourceSeed}</code>
                    </Copyable>
                </td>
            </tr>

            <tr>
                <td>Source Owner</td>
                <td className="text-lg-end">
                    <Address pubkey={info.sourceOwner} alignRight link />
                </td>
            </tr>
        </InstructionCard>
    );
}


