hooks/useTreasuryInfo/groupDomainsByWallet.ts
=============================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { Domain } from '@models/treasury/Domain'

export function groupDomainsByWallet(domains: Domain[]) {
  return domains.reduce((acc, domain) => {
    if (!acc[domain.owner]) {
      acc[domain.owner] = []
    }
    acc[domain.owner].push(domain)

    return acc
  }, {} as { [wallet: string]: Domain[] })
}


