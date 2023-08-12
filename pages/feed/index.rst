pages/feed/index.tsx
====================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import Head from 'next/head'

import { MyFeed } from '@hub/components/MyFeed'

export default function Feed() {
  return (
    <div>
      <Head>
        <title>Ecosystem</title>
        <meta property="og:title" content="Solana Ecosystem" key="title" />
      </Head>
      <MyFeed />
    </div>
  )
}


