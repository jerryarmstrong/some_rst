src/fetchUrlSchemaFile.tsx
==========================

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: tsx

    export default async () => {
  const response = await fetch("https://rpc-devnet.aws.metaplex.com/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      jsonrpc: "2.0",
      method: "schema",
      id: "rpd-op-123",
    }),
  });

  if (response.status === 404) {
    throw new Error("404: Not Found");
  }

  const { result } = await response.json();
  return JSON.stringify(result);
};


