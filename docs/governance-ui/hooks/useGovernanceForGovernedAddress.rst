hooks/useGovernanceForGovernedAddress.ts
========================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js'
import { useMemo } from 'react'
import useGovernanceAssets from './useGovernanceAssets'

const useGovernanceForGovernedAddress = (pubkey?: PublicKey) => {
  const { assetAccounts } = useGovernanceAssets()
  const assetAccount = useMemo(
    () => pubkey && assetAccounts.find((x) => x.pubkey.equals(pubkey)),
    [assetAccounts, pubkey]
  )
  return assetAccount?.governance
}

export default useGovernanceForGovernedAddress


