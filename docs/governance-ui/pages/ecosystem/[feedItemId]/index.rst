pages/ecosystem/[feedItemId]/index.tsx
======================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import Head from 'next/head'
import { useRouter } from 'next/router'

import { FeedItem } from '@hub/components/FeedItem'

export default function EcosystemFeedItem() {
  const router = useRouter()
  const { feedItemId } = router.query

  return (
    <div>
      <Head>
        <title>Realm</title>
        <meta property="og:title" content="Realm" key="title" />
      </Head>
      <FeedItem feedItemId={feedItemId as string} realmUrlId="ecosystem" />
    </div>
  )
}


