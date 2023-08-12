hooks/useGovernanceForGovernedAddress.ts
========================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { PublicKey } from '@solana/web3.js'
import { useMemo } from 'react'
import useGovernanceAssets from './useGovernanceAssets'

const useGovernanceForGovernedAddress = (pubkey: PublicKey | undefined) => {
  const { assetAccounts } = useGovernanceAssets()
  const assetAccount = useMemo(
    () => pubkey && assetAccounts.find((x) => x.pubkey.equals(pubkey)),
    [assetAccounts, pubkey]
  )
  return assetAccount?.governance
}

export default useGovernanceForGovernedAddress


