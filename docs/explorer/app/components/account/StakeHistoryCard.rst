app/components/account/StakeHistoryCard.tsx
===========================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { Epoch } from '@components/common/Epoch';
import { SolBalance } from '@components/common/SolBalance';
import { StakeHistoryEntry, StakeHistoryInfo, SysvarAccount } from '@validators/accounts/sysvar';
import React from 'react';

export function StakeHistoryCard({ sysvarAccount }: { sysvarAccount: SysvarAccount }) {
    const stakeHistory = sysvarAccount.info as StakeHistoryInfo;
    return (
        <>
            <div className="card">
                <div className="card-header">
                    <div className="row align-items-center">
                        <div className="col">
                            <h3 className="card-header-title">Stake History</h3>
                        </div>
                    </div>
                </div>

                <div className="table-responsive mb-0">
                    <table className="table table-sm table-nowrap card-table">
                        <thead>
                            <tr>
                                <th className="w-1 text-muted">Epoch</th>
                                <th className="text-muted">Effective (SOL)</th>
                                <th className="text-muted">Activating (SOL)</th>
                                <th className="text-muted">Deactivating (SOL)</th>
                            </tr>
                        </thead>
                        <tbody className="list">
                            {stakeHistory.length > 0 &&
                                stakeHistory.map((entry: StakeHistoryEntry, index) => {
                                    return renderAccountRow(entry, index);
                                })}
                        </tbody>
                    </table>
                </div>

                <div className="card-footer">
                    <div className="text-muted text-center">
                        {stakeHistory.length > 0 ? '' : 'No stake history found'}
                    </div>
                </div>
            </div>
        </>
    );
}

const renderAccountRow = (entry: StakeHistoryEntry, index: number) => {
    return (
        <tr key={index}>
            <td className="w-1 font-monospace">
                <Epoch epoch={entry.epoch} link />
            </td>
            <td className="font-monospace">
                <SolBalance lamports={entry.stakeHistory.effective} />
            </td>
            <td className="font-monospace">
                <SolBalance lamports={entry.stakeHistory.activating} />
            </td>
            <td className="font-monospace">
                <SolBalance lamports={entry.stakeHistory.deactivating} />
            </td>
        </tr>
    );
};


