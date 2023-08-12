packages/starter/nextjs-starter/src/pages/api/hello.ts
======================================================

Last edited: 2022-10-02 20:43:04

Contents:

.. code-block:: ts

    // Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from 'next';

type Data = {
    name: string;
};

export default function handler(req: NextApiRequest, res: NextApiResponse<Data>) {
    res.status(200).json({ name: 'John Doe' });
}


