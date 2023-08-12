pages/ecosystem/index.tsx
=========================

Last edited: 2023-08-11 18:13:34

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


