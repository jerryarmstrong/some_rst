app/components/instruction/TokenLendingDetailsCard.tsx
======================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { useCluster } from '@providers/cluster';
import { SignatureResult, TransactionInstruction } from '@solana/web3.js';
import { reportError } from '@utils/sentry';
import React from 'react';

import { InstructionCard } from './InstructionCard';
import { parseTokenLendingInstructionTitle } from './token-lending/types';

export function TokenLendingDetailsCard({
    ix,
    index,
    result,
    signature,
    innerCards,
    childIndex,
}: {
    ix: TransactionInstruction;
    index: number;
    result: SignatureResult;
    signature: string;
    innerCards?: JSX.Element[];
    childIndex?: number;
}) {
    const { url } = useCluster();

    let title;
    try {
        title = parseTokenLendingInstructionTitle(ix);
    } catch (error) {
        reportError(error, {
            signature: signature,
            url: url,
        });
    }

    return (
        <InstructionCard
            ix={ix}
            index={index}
            result={result}
            title={`Token Lending: ${title || 'Unknown'}`}
            innerCards={innerCards}
            childIndex={childIndex}
            defaultRaw
        />
    );
}


