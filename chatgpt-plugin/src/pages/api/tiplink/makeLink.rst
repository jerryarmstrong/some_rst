chatgpt-plugin/src/pages/api/tiplink/makeLink.ts
================================================

Last edited: 2023-08-04 21:04:21

Contents:

.. code-block:: ts

    import { NextApiRequest, NextApiResponse } from "next";
import { TipLink } from "@tiplink/api";

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method != "POST") {
    res.status(405).send({ message: "Only POST requests allowed" });
    return;
  }

  const tp = await TipLink.create();
  res.status(200).send({ url: tp.url, tipLinkAddress: tp.keypair.publicKey.toBase58() });
}


