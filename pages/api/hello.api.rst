pages/api/hello.api.ts
======================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    // Next.js API route support: https://nextjs.org/docs/api-routes/introduction

import { withSentry } from '@sentry/nextjs'
import { NextApiRequest, NextApiResponse } from 'next'

const handler = (req: NextApiRequest, res: NextApiResponse) => {
  res.status(200).json({ name: 'John Doe' })
}

export default withSentry(handler)


