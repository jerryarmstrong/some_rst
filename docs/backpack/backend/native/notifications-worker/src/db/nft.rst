backend/native/notifications-worker/src/db/nft.ts
=================================================

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

export const getAllUsersFromPubkey = async (
  pubKeys: string[]
): Promise<string[]> => {
  const response = await chain("query")(
    {
      auth_users: [
        {
          where: {
            public_keys: {
              public_key: { _in: pubKeys },
            },
          },
        },
        {
          id: true,
        },
      ],
    },
    { operationName: "getAllUsersFromPubkey" }
  );
  return response.auth_users.map((x) => x.id);
};

export const getAllUsersInCollection = async (collectionId: string) => {
  const response = await chain("query")(
    {
      auth_user_nfts: [
        {
          where: {
            _or: [
              { collection_id: { _eq: collectionId } },
              { centralized_group: { _eq: collectionId } },
            ],
          },
        },
        {
          public_key: true,
        },
      ],
    },
    { operationName: "getAllUsersInCollection" }
  );

  const uuids = await getAllUsersFromPubkey(
    response.auth_user_nfts.map((x) => x.public_key)
  );
  return uuids;
};


