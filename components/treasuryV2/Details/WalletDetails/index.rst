components/treasuryV2/Details/WalletDetails/index.tsx
=====================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import React from 'react'
import cx from 'classnames'

import { Wallet } from '@models/treasury/Wallet'

import Header from './Header'
import Info from './Info'
import StickyScrolledContainer from '../StickyScrolledContainer'

interface Props {
  className?: string
  wallet: Wallet
  isStickied?: boolean
}

export default function WalletDetails(props: Props) {
  return (
    <div className={cx(props.className, 'rounded', 'overflow-hidden')}>
      <StickyScrolledContainer
        className="h-full"
        isAncestorStickied={props.isStickied}
      >
        <Header wallet={props.wallet} />
        <Info
          className="p-6"
          wallet={props.wallet}
          key={props.wallet.address}
        />
      </StickyScrolledContainer>
    </div>
  )
}


