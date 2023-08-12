app/components/instruction/serum/SweepFeesDetails.tsx
=====================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import React from 'react';

import { InstructionCard } from '../InstructionCard';
import { SerumIxDetailsProps, SweepFees } from './types';

export function SweepFeesDetailsCard(props: SerumIxDetailsProps<SweepFees>) {
    const { ix, index, result, programName, info, innerCards, childIndex } = props;

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title={`${programName} Program: Sweep Fees`}
            innerCards={innerCards}
            childIndex={childIndex}
        >
            <tr>
                <td>Program</td>
                <td className="text-lg-end">
                    <Address pubkey={info.programId} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Market</td>
                <td className="text-lg-end">
                    <Address pubkey={info.accounts.market} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Quote Vault</td>
                <td className="text-lg-end">
                    <Address pubkey={info.accounts.quoteVault} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Fee Sweeping Authority</td>
                <td className="text-lg-end">
                    <Address pubkey={info.accounts.feeSweepingAuthority} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Fee Receiver</td>
                <td className="text-lg-end">
                    <Address pubkey={info.accounts.quoteFeeReceiver} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Vault Signer</td>
                <td className="text-lg-end">
                    <Address pubkey={info.accounts.vaultSigner} alignRight link />
                </td>
            </tr>
        </InstructionCard>
    );
}


