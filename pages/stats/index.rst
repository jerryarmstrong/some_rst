pages/stats/index.tsx
=====================

Last edited: 2023-08-11 18:13:34

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


