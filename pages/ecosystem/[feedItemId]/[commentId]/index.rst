pages/ecosystem/[feedItemId]/[commentId]/index.tsx
==================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import Head from 'next/head'
import { useRouter } from 'next/router'

import { FeedItemComment } from '@hub/components/FeedItemComment'

export default function EcosystemFeedItemComment() {
  const router = useRouter()
  const { feedItemId, commentId } = router.query

  return (
    <div>
      <Head>
        <title>Realm</title>
        <meta property="og:title" content="Realm" key="title" />
      </Head>
      <FeedItemComment
        commentId={commentId as string}
        feedItemId={feedItemId as string}
        realmUrlId="ecosystem"
      />
    </div>
  )
}


