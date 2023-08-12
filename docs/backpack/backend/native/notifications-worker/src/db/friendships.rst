backend/native/notifications-worker/src/db/friendships.ts
=========================================================

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

export const getFriendship = async ({ room }: { room: number }) => {
  const response = await chain("query")(
    {
      auth_friendships: [
        {
          where: {
            id: { _eq: room },
          },
        },
        {
          id: true,
          are_friends: true,
          user1: true,
          user2: true,
          last_message_sender: true,
          user1_last_read_message_id: true,
          user2_last_read_message_id: true,
        },
      ],
    },
    { operationName: "getFriendship" }
  );
  return response.auth_friendships[0] ?? null;
};


