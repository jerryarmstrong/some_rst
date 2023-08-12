packages/metavinci/src/components/ArtistCard/index.tsx
======================================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: tsx

    import React from 'react'
import { useHistory } from 'react-router-dom'
import { Card } from 'antd'

import { Artist } from '../../types'

import './index.less'

export const ArtistCard = ({artist}: {artist: Artist}) => {
  const history = useHistory()

  const handleCoverClick = async () => {
    history.push(artist.link)
  }

  return (
    <Card
      className="artist-card"
      cover={<img alt={artist.name} src={artist.image} onClick={handleCoverClick} />}
    >
      <div>{artist.name}</div>
      <div style={{color: "#ffd691"}}>{artist.itemsAvailable} items available</div>
      <div style={{color: "#82dfd5"}}>{artist.itemsSold} sold</div>
    </Card> 
  )
}


