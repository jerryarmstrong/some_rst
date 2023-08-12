pages/stats/index.tsx
=====================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import Head from 'next/head'
import { GlobalStats } from '@hub/components/GlobalStats'

export default function Stats() {
  return (
    <>
      <Head>
        <title>Realm</title>
        <meta property="og:title" content="Realm" key="title" />
      </Head>
      <GlobalStats />
    </>
  )
}


