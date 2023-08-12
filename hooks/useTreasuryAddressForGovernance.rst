hooks/useTreasuryAddressForGovernance.ts
========================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { getNativeTreasuryAddress } from '@solana/spl-governance'
import { useAsync } from 'react-async-hook'
import { useRealmQuery } from './queries/realm'
import { PublicKey } from '@solana/web3.js'

const useTreasuryAddressForGovernance = (governance: PublicKey | undefined) => {
  const realm = useRealmQuery().data?.result

  return useAsync(
    async () =>
      governance && realm?.owner
        ? await getNativeTreasuryAddress(realm.owner, governance)
        : undefined,
    [governance, realm?.owner]
  )
}

export default useTreasuryAddressForGovernance


