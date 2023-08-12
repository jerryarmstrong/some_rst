backend/native/backend-ws/src/db/chats.ts
=========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { Chain } from "@coral-xyz/chat-zeus";
import type { SubscriptionType } from "@coral-xyz/common";

import { CHAT_HASURA_URL, CHAT_JWT } from "../config";

const chain = Chain(CHAT_HASURA_URL, {
  headers: {
    Authorization: `Bearer ${CHAT_JWT}`,
  },
});

export const getChats = async (
  roomId: string,
  type: SubscriptionType,
  limit = 50,
  offset = 0
) => {
  const response = await chain("query")(
    {
      chats: [
        {
          limit: limit,
          offset: offset,
          //@ts-ignore
          order_by: [{ created_at: "desc" }],
          where: {
            room: { _eq: roomId },
            //@ts-ignore
            type: { _eq: type },
          },
        },
        {
          id: true,
          uuid: true,
          message: true,
          client_generated_uuid: true,
          created_at: true,
          message_kind: true,
          parent_client_generated_uuid: true,
        },
      ],
    },
    { operationName: "getChats" }
  );
  return response.chats || [];
};


