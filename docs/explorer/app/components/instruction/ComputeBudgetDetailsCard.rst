app/components/instruction/ComputeBudgetDetailsCard.tsx
=======================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { SolBalance } from '@components/common/SolBalance';
import { useCluster } from '@providers/cluster';
import { ComputeBudgetInstruction, SignatureResult, TransactionInstruction } from '@solana/web3.js';
import { microLamportsToLamportsString } from '@utils/index';
import { reportError } from '@utils/sentry';
import React from 'react';

import { InstructionCard } from './InstructionCard';

export function ComputeBudgetDetailsCard({
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
    try {
        const type = ComputeBudgetInstruction.decodeInstructionType(ix);
        switch (type) {
            case 'RequestUnits': {
                const { units, additionalFee } = ComputeBudgetInstruction.decodeRequestUnits(ix);
                return (
                    <InstructionCard
                        ix={ix}
                        index={index}
                        result={result}
                        title="Compute Budget Program: Request Units (Deprecated)"
                        innerCards={innerCards}
                        childIndex={childIndex}
                    >
                        <tr>
                            <td>Program</td>
                            <td className="text-lg-end">
                                <Address pubkey={ix.programId} alignRight link />
                            </td>
                        </tr>

                        <tr>
                            <td>Requested Compute Units</td>
                            <td className="text-lg-end font-monospace">{`${new Intl.NumberFormat('en-US').format(
                                units
                            )} compute units`}</td>
                        </tr>

                        <tr>
                            <td>Additional Fee (SOL)</td>
                            <td className="text-lg-end">
                                <SolBalance lamports={additionalFee} />
                            </td>
                        </tr>
                    </InstructionCard>
                );
            }
            case 'RequestHeapFrame': {
                const { bytes } = ComputeBudgetInstruction.decodeRequestHeapFrame(ix);
                return (
                    <InstructionCard
                        ix={ix}
                        index={index}
                        result={result}
                        title="Compute Budget Program: Request Heap Frame"
                        innerCards={innerCards}
                        childIndex={childIndex}
                    >
                        <tr>
                            <td>Program</td>
                            <td className="text-lg-end">
                                <Address pubkey={ix.programId} alignRight link />
                            </td>
                        </tr>

                        <tr>
                            <td>Requested Heap Frame (Bytes)</td>
                            <td className="text-lg-end font-monospace">
                                {new Intl.NumberFormat('en-US').format(bytes)}
                            </td>
                        </tr>
                    </InstructionCard>
                );
            }
            case 'SetComputeUnitLimit': {
                const { units } = ComputeBudgetInstruction.decodeSetComputeUnitLimit(ix);
                return (
                    <InstructionCard
                        ix={ix}
                        index={index}
                        result={result}
                        title="Compute Budget Program: Set Compute Unit Limit"
                        innerCards={innerCards}
                        childIndex={childIndex}
                    >
                        <tr>
                            <td>Program</td>
                            <td className="text-lg-end">
                                <Address pubkey={ix.programId} alignRight link />
                            </td>
                        </tr>

                        <tr>
                            <td>Compute Unit Limit</td>
                            <td className="text-lg-end font-monospace">{`${new Intl.NumberFormat('en-US').format(
                                units
                            )} compute units`}</td>
                        </tr>
                    </InstructionCard>
                );
            }
            case 'SetComputeUnitPrice': {
                const { microLamports } = ComputeBudgetInstruction.decodeSetComputeUnitPrice(ix);
                return (
                    <InstructionCard
                        ix={ix}
                        index={index}
                        result={result}
                        title="Compute Budget Program: Set Compute Unit Price"
                        innerCards={innerCards}
                        childIndex={childIndex}
                    >
                        <tr>
                            <td>Program</td>
                            <td className="text-lg-end">
                                <Address pubkey={ix.programId} alignRight link />
                            </td>
                        </tr>

                        <tr>
                            <td>Compute Unit Price</td>
                            <td className="text-lg-end font-monospace">{`${microLamportsToLamportsString(
                                microLamports
                            )} lamports per compute unit`}</td>
                        </tr>
                    </InstructionCard>
                );
            }
        }
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
            title="Compute Budget Program: Unknown Instruction"
            innerCards={innerCards}
            childIndex={childIndex}
            defaultRaw
        />
    );
}


