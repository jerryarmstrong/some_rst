models/treasury/Program.ts
==========================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    import type { AssetAccount } from '@utils/uiTypes/assets'

export interface Program {
  address: string
  lastDeployedSlot: number
  upgradeAuthority?: string
  walletIsUpgradeAuthority: boolean
  raw: AssetAccount
}


