pages/ecosystem/index.tsx
=========================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import Head from 'next/head'

import { EcosystemFeed } from '@hub/components/EcosystemFeed'

export default function Ecosystem() {
  return (
    <div>
      <Head>
        <title>Ecosystem</title>
        <meta property="og:title" content="Solana Ecosystem" key="title" />
      </Head>
      <EcosystemFeed />
    </div>
  )
}


