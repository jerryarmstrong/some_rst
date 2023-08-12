components/treasuryV2/Details/NFTCollectionDetails/Info/Overview/index.tsx
==========================================================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import React from 'react'
import cx from 'classnames'

import { NFTCollection } from '@models/treasury/Asset'

import NFT from './NFT'

interface Props {
  className?: string
  nftCollection: NFTCollection
}

export default function Overview(props: Props) {
  return (
    <section
      className={cx(
        props.className,
        'gap-7',
        'grid',
        'grid-cols-2',
        'xl:grid-cols-3'
      )}
    >
      {props.nftCollection.list.map((nft) => (
        <NFT key={nft.address} nft={nft} />
      ))}
    </section>
  )
}


