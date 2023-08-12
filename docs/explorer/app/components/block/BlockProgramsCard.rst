app/components/block/BlockProgramsCard.tsx
==========================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Address } from '@components/common/Address';
import { TableCardBody } from '@components/common/TableCardBody';
import { PublicKey, VersionedBlockResponse } from '@solana/web3.js';
import React from 'react';

export function BlockProgramsCard({ block }: { block: VersionedBlockResponse }) {
    const totalTransactions = block.transactions.length;
    const txSuccesses = new Map<string, number>();
    const txFrequency = new Map<string, number>();
    const ixFrequency = new Map<string, number>();

    let totalInstructions = 0;
    block.transactions.forEach(tx => {
        const message = tx.transaction.message;
        totalInstructions += message.compiledInstructions.length;
        const programUsed = new Set<string>();
        const accountKeys = tx.transaction.message.getAccountKeys({
            accountKeysFromLookups: tx.meta?.loadedAddresses,
        });
        const trackProgram = (index: number) => {
            if (index >= accountKeys.length) return;
            const programId = accountKeys.get(index)!;
            const programAddress = programId.toBase58();
            programUsed.add(programAddress);
            const frequency = ixFrequency.get(programAddress);
            ixFrequency.set(programAddress, frequency ? frequency + 1 : 1);
        };

        message.compiledInstructions.forEach(ix => trackProgram(ix.programIdIndex));
        tx.meta?.innerInstructions?.forEach(inner => {
            totalInstructions += inner.instructions.length;
            inner.instructions.forEach(innerIx => trackProgram(innerIx.programIdIndex));
        });

        const successful = tx.meta?.err === null;
        programUsed.forEach(programId => {
            const frequency = txFrequency.get(programId);
            txFrequency.set(programId, frequency ? frequency + 1 : 1);
            if (successful) {
                const count = txSuccesses.get(programId);
                txSuccesses.set(programId, count ? count + 1 : 1);
            }
        });
    });

    const programEntries: [string, number][] = [];
    txFrequency.forEach((txFreq, programId) => {
        programEntries.push([programId, txFreq]);
    });

    programEntries.sort((a, b) => {
        if (a[1] < b[1]) return 1;
        if (a[1] > b[1]) return -1;
        return 0;
    });

    const showSuccessRate = block.transactions.every(tx => tx.meta !== null);
    return (
        <>
            <div className="card">
                <div className="card-header align-items-center">
                    <h3 className="card-header-title">Block Program Stats</h3>
                </div>
                <TableCardBody>
                    <tr>
                        <td className="w-100">Unique Programs Count</td>
                        <td className="text-lg-end font-monospace">{programEntries.length}</td>
                    </tr>
                    <tr>
                        <td className="w-100">Total Instructions</td>
                        <td className="text-lg-end font-monospace">{totalInstructions}</td>
                    </tr>
                </TableCardBody>
            </div>
            <div className="card">
                <div className="card-header align-items-center">
                    <h3 className="card-header-title">Block Programs</h3>
                </div>

                <div className="table-responsive mb-0">
                    <table className="table table-sm table-nowrap card-table">
                        <thead>
                            <tr>
                                <th className="text-muted">Program</th>
                                <th className="text-muted">Transaction Count</th>
                                <th className="text-muted">% of Total</th>
                                <th className="text-muted">Instruction Count</th>
                                <th className="text-muted">% of Total</th>
                                {showSuccessRate && <th className="text-muted">Success Rate</th>}
                            </tr>
                        </thead>
                        <tbody>
                            {programEntries.map(([programId, txFreq]) => {
                                const ixFreq = ixFrequency.get(programId) as number;
                                const successes = txSuccesses.get(programId) || 0;
                                return (
                                    <tr key={programId}>
                                        <td>
                                            <Address pubkey={new PublicKey(programId)} link />
                                        </td>
                                        <td>{txFreq}</td>
                                        <td>{((100 * txFreq) / totalTransactions).toFixed(2)}%</td>
                                        <td>{ixFreq}</td>
                                        <td>{((100 * ixFreq) / totalInstructions).toFixed(2)}%</td>
                                        {showSuccessRate && <td>{((100 * successes) / txFreq).toFixed(0)}%</td>}
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>
            </div>
        </>
    );
}


