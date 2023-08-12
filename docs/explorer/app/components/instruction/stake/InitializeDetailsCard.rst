app/components/instruction/stake/InitializeDetailsCard.tsx
==========================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { Epoch } from '@components/common/Epoch';
import { ParsedInstruction, SignatureResult, StakeProgram, SystemProgram } from '@solana/web3.js';
import { displayTimestampUtc } from '@utils/date';
import React from 'react';

import { InstructionCard } from '../InstructionCard';
import { InitializeInfo } from './types';

export function InitializeDetailsCard(props: {
    ix: ParsedInstruction;
    index: number;
    result: SignatureResult;
    info: InitializeInfo;
    innerCards?: JSX.Element[];
    childIndex?: number;
}) {
    const { ix, index, result, info, innerCards, childIndex } = props;

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title="Stake Program: Initialize Stake"
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
                <td>Stake Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.stakeAccount} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Stake Authority Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.authorized.staker} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Withdraw Authority Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.authorized.withdrawer} alignRight link />
                </td>
            </tr>

            {info.lockup.epoch > 0 && (
                <tr>
                    <td>Lockup Expiry Epoch</td>
                    <td className="text-lg-end">
                        <Epoch epoch={info.lockup.epoch} link />
                    </td>
                </tr>
            )}

            {info.lockup.unixTimestamp > 0 && (
                <tr>
                    <td>Lockup Expiry Timestamp</td>
                    <td className="text-lg-end font-monospace">
                        {displayTimestampUtc(info.lockup.unixTimestamp * 1000)}
                    </td>
                </tr>
            )}

            {!info.lockup.custodian.equals(SystemProgram.programId) && (
                <tr>
                    <td>Lockup Custodian Address</td>
                    <td className="text-lg-end">
                        <Address pubkey={info.lockup.custodian} alignRight link />
                    </td>
                </tr>
            )}
        </InstructionCard>
    );
}


