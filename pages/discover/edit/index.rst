pages/discover/edit/index.tsx
=============================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import Head from 'next/head'
import { EditDiscoverPage } from '@hub/components/EditDiscoverPage'

export default function Stats() {
  return (
    <>
      <Head>
        <title>Edit Discover</title>
        <meta property="og:title" content="Edit Discover" key="title" />
      </Head>
      <EditDiscoverPage className="py-40 max-w-7xl mx-auto px-10" />
    </>
  )
}


