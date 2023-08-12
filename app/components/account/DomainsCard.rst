app/components/account/DomainsCard.tsx
======================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    'use client';

import { Address } from '@components/common/Address';
import { ErrorCard } from '@components/common/ErrorCard';
import { LoadingCard } from '@components/common/LoadingCard';
import { useUserDomains } from '@utils/name-service';
import React from 'react';

import { DomainInfo } from '@/app/utils/domain-info';

export function DomainsCard({ address }: { address: string }) {
    const [domains, domainsLoading] = useUserDomains(address);

    if (domainsLoading && (!domains || domains.length === 0)) {
        return <LoadingCard message="Loading domains" />;
    } else if (!domains) {
        return <ErrorCard text="Failed to fetch domains" />;
    }

    if (domains.length === 0) {
        return <ErrorCard text="No domain name found" />;
    }

    return (
        <div className="card">
            <div className="card-header align-items-center">
                <h3 className="card-header-title">Owned Domain Names</h3>
            </div>
            <div className="table-responsive mb-0">
                <table className="table table-sm table-nowrap card-table">
                    <thead>
                        <tr>
                            <th className="text-muted">Domain Name</th>
                            <th className="text-muted">Name Service Account</th>
                        </tr>
                    </thead>
                    <tbody className="list">
                        {domains.map(domain => (
                            <RenderDomainRow key={domain.address.toBase58()} domainInfo={domain} />
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

function RenderDomainRow({ domainInfo }: { domainInfo: DomainInfo }) {
    return (
        <tr>
            <td>{domainInfo.name}</td>
            <td>
                <Address pubkey={domainInfo.address} link />
            </td>
        </tr>
    );
}


