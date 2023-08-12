components/treasuryV2/Details/WalletDetails/Info/Dashboard.tsx
==============================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import React from 'react'
import cx from 'classnames'

import { Wallet } from '@models/treasury/Wallet'

import Activity from '../../TokenDetails/Activity'
import Statistics from './Statistics'

interface Props {
  className?: string
  wallet: Wallet
}

export default function Dashboard(props: Props) {
  return (
    <div className={cx(props.className, 'space-y-12')}>
      <Statistics statistics={props.wallet.stats} />
      <Activity
        assets={[
          { address: props.wallet.address },
          ...(props.wallet.governanceAddress
            ? [{ address: props.wallet.governanceAddress }]
            : []),
        ]}
        title="Wallet Activity"
      />
    </div>
  )
}


