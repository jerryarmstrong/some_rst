backend/native/backend-ws/src/db/publicKeys.ts
==============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { Chain } from "@coral-xyz/zeus";

import { AUTH_HASURA_URL, AUTH_JWT } from "../config";

const chain = Chain(AUTH_HASURA_URL, {
  headers: {
    Authorization: `Bearer ${AUTH_JWT}`,
  },
});

export const getPublicKeys = async (uuid: string) => {
  const response = await chain("query")(
    {
      auth_public_keys: [
        {
          where: {
            user_id: { _eq: uuid },
          },
          limit: 100,
        },
        {
          public_key: true,
        },
      ],
    },
    { operationName: "getPublicKeys" }
  );
  return response.auth_public_keys.map((x) => x.public_key);
};


