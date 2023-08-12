examples/js/ui-create-nft-with-derived-signer/pages/api/hello.ts
================================================================

Last edited: 2023-08-11 07:39:15

Contents:

.. code-block:: ts

    // Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next'

type Data = {
  name: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  res.status(200).json({ name: 'John Doe' })
}


