app/components/instruction/serum/DisableMarketDetails.tsx
=========================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import React from 'react';

import { InstructionCard } from '../InstructionCard';
import { DisableMarket, SerumIxDetailsProps } from './types';

export function DisableMarketDetailsCard(props: SerumIxDetailsProps<DisableMarket>) {
    const { ix, index, result, programName, info, innerCards, childIndex } = props;

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title={`${programName} Program: Disable Market`}
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
                <td>Disable Authority</td>
                <td className="text-lg-end">
                    <Address pubkey={info.accounts.disableAuthority} alignRight link />
                </td>
            </tr>
        </InstructionCard>
    );
}


