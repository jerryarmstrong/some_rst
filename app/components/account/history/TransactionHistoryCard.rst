app/components/account/history/TransactionHistoryCard.tsx
=========================================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    'use client';

import { ErrorCard } from '@components/common/ErrorCard';
import { LoadingCard } from '@components/common/LoadingCard';
import { Signature } from '@components/common/Signature';
import { Slot } from '@components/common/Slot';
import { useAccountHistory, useFetchAccountHistory } from '@providers/accounts/history';
import { FetchStatus } from '@providers/cache';
import { PublicKey } from '@solana/web3.js';
import { displayTimestampUtc } from '@utils/date';
import React, { useMemo } from 'react';
import Moment from 'react-moment';

import { getTransactionRows, HistoryCardFooter, HistoryCardHeader } from '../HistoryCardComponents';

export function TransactionHistoryCard({ address }: { address: string }) {
    const pubkey = useMemo(() => new PublicKey(address), [address]);
    const history = useAccountHistory(address);
    const fetchAccountHistory = useFetchAccountHistory();
    const refresh = () => fetchAccountHistory(pubkey, false, true);
    const loadMore = () => fetchAccountHistory(pubkey, false);

    const transactionRows = React.useMemo(() => {
        if (history?.data?.fetched) {
            return getTransactionRows(history.data.fetched);
        }
        return [];
    }, [history]);

    React.useEffect(() => {
        if (!history) {
            refresh();
        }
    }, [address]); // eslint-disable-line react-hooks/exhaustive-deps

    if (!history) {
        return null;
    }

    if (history?.data === undefined) {
        if (history.status === FetchStatus.Fetching) {
            return <LoadingCard message="Loading history" />;
        }

        return <ErrorCard retry={refresh} text="Failed to fetch transaction history" />;
    }

    const hasTimestamps = transactionRows.some(element => element.blockTime);
    const detailsList: React.ReactNode[] = transactionRows.map(
        ({ slot, signature, blockTime, statusClass, statusText }) => {
            return (
                <tr key={signature}>
                    <td>
                        <Signature signature={signature} link truncateChars={60} />
                    </td>

                    <td className="w-1">
                        <Slot slot={slot} link />
                    </td>

                    {hasTimestamps && (
                        <>
                            <td className="text-muted">
                                {blockTime ? <Moment date={blockTime * 1000} fromNow /> : '---'}
                            </td>
                            <td className="text-muted">
                                {blockTime ? displayTimestampUtc(blockTime * 1000, true) : '---'}
                            </td>
                        </>
                    )}

                    <td>
                        <span className={`badge bg-${statusClass}-soft`}>{statusText}</span>
                    </td>
                </tr>
            );
        }
    );

    const fetching = history.status === FetchStatus.Fetching;
    return (
        <div className="card">
            <HistoryCardHeader fetching={fetching} refresh={() => refresh()} title="Transaction History" />
            <div className="table-responsive mb-0">
                <table className="table table-sm table-nowrap card-table">
                    <thead>
                        <tr>
                            <th className="text-muted w-1">Transaction Signature</th>
                            <th className="text-muted w-1">Block</th>
                            {hasTimestamps && (
                                <>
                                    <th className="text-muted w-1">Age</th>
                                    <th className="text-muted w-1">Timestamp</th>
                                </>
                            )}
                            <th className="text-muted">Result</th>
                        </tr>
                    </thead>
                    <tbody className="list">{detailsList}</tbody>
                </table>
            </div>
            <HistoryCardFooter fetching={fetching} foundOldest={history.data.foundOldest} loadMore={() => loadMore()} />
        </div>
    );
}


