app/components/account/VoteAccountSection.tsx
=============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { AccountAddressRow, AccountBalanceRow, AccountHeader } from '@components/common/Account';
import { Address } from '@components/common/Address';
import { Slot } from '@components/common/Slot';
import { TableCardBody } from '@components/common/TableCardBody';
import { Account, useFetchAccountInfo } from '@providers/accounts';
import { displayTimestamp } from '@utils/date';
import { VoteAccount } from '@validators/accounts/vote';
import React from 'react';

export function VoteAccountSection({ account, voteAccount }: { account: Account; voteAccount: VoteAccount }) {
    const refresh = useFetchAccountInfo();
    const rootSlot = voteAccount.info.rootSlot;
    return (
        <div className="card">
            <AccountHeader title="Vote Account" refresh={() => refresh(account.pubkey, 'parsed')} />

            <TableCardBody>
                <AccountAddressRow account={account} />
                <AccountBalanceRow account={account} />

                <tr>
                    <td>
                        Authorized Voter
                        {voteAccount.info.authorizedVoters.length > 1 ? 's' : ''}
                    </td>
                    <td className="text-lg-end">
                        {voteAccount.info.authorizedVoters.map(voter => {
                            return (
                                <Address
                                    pubkey={voter.authorizedVoter}
                                    key={voter.authorizedVoter.toString()}
                                    alignRight
                                    raw
                                    link
                                />
                            );
                        })}
                    </td>
                </tr>

                <tr>
                    <td>Authorized Withdrawer</td>
                    <td className="text-lg-end">
                        <Address pubkey={voteAccount.info.authorizedWithdrawer} alignRight raw link />
                    </td>
                </tr>

                <tr>
                    <td>Last Timestamp</td>
                    <td className="text-lg-end font-monospace">
                        {displayTimestamp(voteAccount.info.lastTimestamp.timestamp * 1000)}
                    </td>
                </tr>

                <tr>
                    <td>Commission</td>
                    <td className="text-lg-end">{voteAccount.info.commission + '%'}</td>
                </tr>

                <tr>
                    <td>Root Slot</td>
                    <td className="text-lg-end">{rootSlot !== null ? <Slot slot={rootSlot} link /> : 'N/A'}</td>
                </tr>
            </TableCardBody>
        </div>
    );
}


