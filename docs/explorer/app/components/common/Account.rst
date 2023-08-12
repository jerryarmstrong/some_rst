app/components/common/Account.tsx
=================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { SolBalance } from '@components/common/SolBalance';
import { Account } from '@providers/accounts';
import React from 'react';
import { RefreshCw } from 'react-feather';

import { Address } from './Address';

type AccountHeaderProps = {
    title: string;
    refresh: () => void;
};

type AccountProps = {
    account: Account;
};

export function AccountHeader({ title, refresh }: AccountHeaderProps) {
    return (
        <div className="card-header align-items-center">
            <h3 className="card-header-title">{title}</h3>
            <button className="btn btn-white btn-sm" onClick={() => refresh()}>
                <RefreshCw className="align-text-top me-2" size={13} />
                Refresh
            </button>
        </div>
    );
}

export function AccountAddressRow({ account }: AccountProps) {
    return (
        <tr>
            <td>Address</td>
            <td className="text-lg-end">
                <Address pubkey={account.pubkey} alignRight raw />
            </td>
        </tr>
    );
}

export function AccountBalanceRow({ account }: AccountProps) {
    const { lamports } = account;
    return (
        <tr>
            <td>Balance (SOL)</td>
            <td className="text-lg-end text-uppercase">
                <SolBalance lamports={lamports} />
            </td>
        </tr>
    );
}


