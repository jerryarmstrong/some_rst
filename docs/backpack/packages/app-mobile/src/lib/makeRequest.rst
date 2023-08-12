packages/app-mobile/src/lib/makeRequest.ts
==========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { BACKEND_API_URL } from "@coral-xyz/common";

async function makeRequest(path: string, options: any) {
  const url = `${BACKEND_API_URL}${path}`;
  return fetch(url, options).then((res) => res.json());
}

export function updateLastRead({
  room,
  type,
  publicKey,
  nftMint,
  client_generated_uuid,
}: any) {
  const path = `/chat/lastRead?room=${room}&type=${type}&publicKey=${publicKey}&mint=${nftMint}`;
  return makeRequest(path, {
    body: JSON.stringify({ client_generated_uuid }),
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
}


