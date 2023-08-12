app/components/instruction/mango/CancelPerpOrderDetailsCard.tsx
===============================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { SignatureResult, TransactionInstruction } from '@solana/web3.js';

import { InstructionCard } from '../InstructionCard';
import { CancelPerpOrder, getPerpMarketFromInstruction } from './types';

export function CancelPerpOrderDetailsCard(props: {
    ix: TransactionInstruction;
    index: number;
    result: SignatureResult;
    info: CancelPerpOrder;
    innerCards?: JSX.Element[];
    childIndex?: number;
}) {
    const { ix, index, result, info, innerCards, childIndex } = props;
    const mangoAccount = ix.keys[1];
    const perpMarketAccountMeta = ix.keys[3];
    const mangoPerpMarketConfig = getPerpMarketFromInstruction(ix, perpMarketAccountMeta);

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title="Mango Program: CancelPerpOrder"
            innerCards={innerCards}
            childIndex={childIndex}
        >
            <tr>
                <td>Mango account</td>
                <td>
                    <Address pubkey={mangoAccount.pubkey} alignRight link />
                </td>
            </tr>

            {mangoPerpMarketConfig !== undefined && (
                <tr>
                    <td>Perp market</td>
                    <td className="text-lg-end">{mangoPerpMarketConfig.name}</td>
                </tr>
            )}

            <tr>
                <td>Perp market address</td>
                <td>
                    <Address pubkey={perpMarketAccountMeta.pubkey} alignRight link />
                </td>
            </tr>

            <tr>
                <td>Order Id</td>
                <td className="text-lg-end">{info.orderId}</td>
            </tr>
        </InstructionCard>
    );
}


