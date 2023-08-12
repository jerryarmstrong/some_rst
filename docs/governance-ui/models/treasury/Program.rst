models/treasury/Program.ts
==========================

Last edited: 2023-05-19 22:20:18

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


