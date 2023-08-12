app/components/instruction/system/NonceInitializeDetailsCard.tsx
================================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { ParsedInstruction, SignatureResult, SystemProgram } from '@solana/web3.js';
import React from 'react';

import { InstructionCard } from '../InstructionCard';
import { InitializeNonceInfo } from './types';

export function NonceInitializeDetailsCard(props: {
    ix: ParsedInstruction;
    index: number;
    result: SignatureResult;
    info: InitializeNonceInfo;
    innerCards?: JSX.Element[];
    childIndex?: number;
}) {
    const { ix, index, result, info, innerCards, childIndex } = props;

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title="System Program: Initialize Nonce"
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
                <td>Nonce Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.nonceAccount} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Authority Address</td>
                <td className="text-lg-end">
                    <Address pubkey={info.nonceAuthority} alignRight link />
                </td>
            </tr>
        </InstructionCard>
    );
}


