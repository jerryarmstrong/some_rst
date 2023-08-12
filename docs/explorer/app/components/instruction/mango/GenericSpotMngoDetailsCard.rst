app/components/instruction/mango/GenericSpotMngoDetailsCard.tsx
===============================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { SignatureResult, TransactionInstruction } from '@solana/web3.js';

import { InstructionCard } from '../InstructionCard';
import { getSpotMarketFromInstruction } from './types';

export function GenericSpotMngoDetailsCard(props: {
    ix: TransactionInstruction;
    index: number;
    result: SignatureResult;
    accountKeyLocation: number;
    spotMarketkeyLocation: number;
    title: string;
    innerCards?: JSX.Element[];
    childIndex?: number;
}) {
    const { ix, index, result, accountKeyLocation, spotMarketkeyLocation, title, innerCards, childIndex } = props;
    const mangoAccount = ix.keys[accountKeyLocation];
    const spotMarketAccountMeta = ix.keys[spotMarketkeyLocation];
    const mangoSpotMarketConfig = getSpotMarketFromInstruction(ix, spotMarketAccountMeta);

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title={'Mango Program: ' + title}
            innerCards={innerCards}
            childIndex={childIndex}
        >
            <tr>
                <td>Mango account</td>
                <td>
                    <Address pubkey={mangoAccount.pubkey} alignRight link />
                </td>
            </tr>

            {mangoSpotMarketConfig !== undefined && (
                <tr>
                    <td>Spot market</td>
                    <td className="text-lg-end">{mangoSpotMarketConfig.name}</td>
                </tr>
            )}

            <tr>
                <td>Spot market address</td>
                <td>
                    <Address pubkey={spotMarketAccountMeta.pubkey} alignRight link />
                </td>
            </tr>
        </InstructionCard>
    );
}


