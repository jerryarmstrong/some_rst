hooks/useTreasuryInfo/calculateTokenCountAndValue.ts
====================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import { BigNumber } from 'bignumber.js'

import { AccountType, AssetAccount } from '@utils/uiTypes/assets'

import { getAccountAssetCount } from './getAccountAssetCount'
import { getAccountValue } from './getAccountValue'

export const calculateTokenCountAndValue = (accounts: AssetAccount[]) => {
  const counts: Map<string, BigNumber> = new Map()
  const values: Map<string, BigNumber> = new Map()

  for (const account of accounts) {
    if (account.type !== AccountType.NFT) {
      const key = account.pubkey.toBase58()
      const count = getAccountAssetCount(account)
      const value = getAccountValue(account)

      counts.set(key, count)
      values.set(key, value)
    }
  }

  return { counts, values }
}


