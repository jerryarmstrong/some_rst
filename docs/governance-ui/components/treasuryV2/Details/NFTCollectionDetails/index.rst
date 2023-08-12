components/treasuryV2/Details/NFTCollectionDetails/index.tsx
============================================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import React from 'react'
import cx from 'classnames'

import { NFTCollection } from '@models/treasury/Asset'

import Header from './Header'
import StickyScrolledContainer from '../StickyScrolledContainer'
import Info from './Info'

interface Props {
  className?: string
  nftCollection: NFTCollection
  isStickied?: boolean
}

export default function MintDetails(props: Props) {
  return (
    <div className={cx(props.className, 'rounded', 'overflow-hidden')}>
      <StickyScrolledContainer
        className="h-full"
        isAncestorStickied={props.isStickied}
      >
        <Header nftCollection={props.nftCollection} />
        <section className="p-6 bg-bkg-3">
          <Info nftCollection={props.nftCollection} />
        </section>
      </StickyScrolledContainer>
    </div>
  )
}


