backend/native/notifications-worker/src/db/notifications.ts
===========================================================

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

export const getSubscriptions = async (uuid: string) => {
  return chain("query")(
    {
      auth_notification_subscriptions: [
        {
          where: { uuid: { _eq: (uuid as string) || "" } },
          limit: 5,
        },
        {
          username: true,
          endpoint: true,
          expirationTime: true,
          p256dh: true,
          auth: true,
          id: true,
        },
      ],
    },
    { operationName: "getSubscriptions" }
  );
};

export const deleteSubscription = (id: number) => {
  return chain("mutation")(
    {
      delete_auth_notification_subscriptions_by_pk: [
        {
          id,
        },
        {
          id: true,
        },
      ],
    },
    { operationName: "deleteSubscription" }
  );
};


