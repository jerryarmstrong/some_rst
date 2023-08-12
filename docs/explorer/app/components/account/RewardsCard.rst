app/components/account/RewardsCard.tsx
======================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    'use client';

import { Epoch } from '@components/common/Epoch';
import { ErrorCard } from '@components/common/ErrorCard';
import { LoadingCard } from '@components/common/LoadingCard';
import { Slot } from '@components/common/Slot';
import { useAccountInfo } from '@providers/accounts';
import { useFetchRewards, useRewards } from '@providers/accounts/rewards';
import { FetchStatus } from '@providers/cache';
import { PublicKey } from '@solana/web3.js';
import { lamportsToSolString } from '@utils/index';
import React from 'react';

const U64_MAX = BigInt('0xffffffffffffffff');

export function RewardsCard({ address }: { address: string }) {
    const pubkey = React.useMemo(() => new PublicKey(address), [address]);
    const info = useAccountInfo(address);
    const account = info?.data;
    const parsedData = account?.data.parsed;

    const highestEpoch = React.useMemo(() => {
        if (!parsedData) return;
        if (parsedData.program !== 'stake') return;
        const stakeInfo = parsedData.parsed.info.stake;
        if (stakeInfo !== null && stakeInfo.delegation.deactivationEpoch !== U64_MAX) {
            return Number(stakeInfo.delegation.deactivationEpoch);
        }
    }, [parsedData]);

    const rewards = useRewards(address);
    const fetchRewards = useFetchRewards();
    const loadMore = () => fetchRewards(pubkey, highestEpoch);

    React.useEffect(() => {
        if (!rewards) {
            fetchRewards(pubkey, highestEpoch);
        }
    }, []); // eslint-disable-line react-hooks/exhaustive-deps

    if (!rewards) {
        return null;
    }

    if (rewards?.data === undefined) {
        if (rewards.status === FetchStatus.Fetching) {
            return <LoadingCard message="Loading rewards" />;
        }

        return <ErrorCard retry={loadMore} text="Failed to fetch rewards" />;
    }

    const rewardsList = rewards.data.rewards.map(reward => {
        if (!reward) {
            return null;
        }

        return (
            <tr key={reward.epoch}>
                <td>
                    <Epoch epoch={reward.epoch} link />
                </td>
                <td>
                    <Slot slot={reward.effectiveSlot} link />
                </td>
                <td>{lamportsToSolString(reward.amount)}</td>
                <td>{lamportsToSolString(reward.postBalance)}</td>
            </tr>
        );
    });
    const rewardsFound = rewardsList.some(r => r);
    const { foundOldest, lowestFetchedEpoch, highestFetchedEpoch } = rewards.data;
    const fetching = rewards.status === FetchStatus.Fetching;

    return (
        <>
            <div className="card">
                <div className="card-header">
                    <div className="row align-items-center">
                        <div className="col">
                            <h3 className="card-header-title">Rewards</h3>
                        </div>
                    </div>
                </div>

                {rewardsFound ? (
                    <div className="table-responsive mb-0">
                        <table className="table table-sm table-nowrap card-table">
                            <thead>
                                <tr>
                                    <th className="w-1 text-muted">Epoch</th>
                                    <th className="text-muted">Effective Slot</th>
                                    <th className="text-muted">Reward Amount</th>
                                    <th className="text-muted">Post Balance</th>
                                </tr>
                            </thead>
                            <tbody className="list">{rewardsList}</tbody>
                        </table>
                    </div>
                ) : (
                    <div className="card-body">
                        No rewards issued between epochs {lowestFetchedEpoch} and {highestFetchedEpoch}
                    </div>
                )}

                <div className="card-footer">
                    {foundOldest ? (
                        <div className="text-muted text-center">Fetched full reward history</div>
                    ) : (
                        <button className="btn btn-primary w-100" onClick={() => loadMore()} disabled={fetching}>
                            {fetching ? (
                                <>
                                    <span className="align-text-top spinner-grow-sm me-2"></span>
                                    Loading
                                </>
                            ) : (
                                'Load More'
                            )}
                        </button>
                    )}
                </div>
            </div>
        </>
    );
}


