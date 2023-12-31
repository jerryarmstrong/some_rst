backend/native/backpack-api/src/db/notifications.ts
===================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import { Chain, order_by } from "@coral-xyz/zeus";

import { HASURA_URL, JWT } from "../config";

const chain = Chain(HASURA_URL, {
  headers: {
    Authorization: `Bearer ${JWT}`,
  },
});

export const getNotifications = async (
  uuid: string,
  offset?: number,
  limit?: number
) => {
  const response = await chain("query")(
    {
      auth_notifications: [
        {
          where: { uuid: { _eq: uuid } },
          limit,
          offset,
          //@ts-ignore
          order_by: [{ id: "desc" }],
        },
        {
          id: true,
          timestamp: true,
          title: true,
          body: true,
          xnft_id: true,
          viewed: true,
        },
      ],
    },
    { operationName: "getNotifications" }
  );
  return response.auth_notifications || [];
};

export const updateCursor = async ({
  uuid,
  lastNotificationId,
}: {
  uuid: string;
  lastNotificationId: number;
}) => {
  const currentCursor = await chain("query")(
    {
      auth_notification_cursor: [
        {
          where: { uuid: { _eq: uuid } },
        },
        {
          last_read_notificaiton: true,
        },
      ],
    },
    { operationName: "updateCursor" }
  );
  const currentCursorId =
    currentCursor.auth_notification_cursor[0]?.last_read_notificaiton;
  if (currentCursorId && currentCursorId >= lastNotificationId) {
    return;
  }
  await chain("mutation")(
    {
      insert_auth_notification_cursor_one: [
        {
          object: {
            uuid,
            last_read_notificaiton: lastNotificationId,
          },
          on_conflict: {
            update_columns: [
              //@ts-ignore
              "last_read_notificaiton",
            ],
            //@ts-ignore
            constraint: "notification_cursor_pkey",
          },
        },
        {
          uuid: true,
        },
      ],
    },
    { operationName: "updateCursor" }
  );
};

export const updateNotificationSeen = async ({
  uuid,
  notificationIds,
}: {
  uuid: string;
  notificationIds: number[];
}) => {
  return chain("mutation")(
    {
      update_auth_notifications: [
        {
          _set: {
            viewed: true,
          },
          where: { id: { _in: notificationIds }, uuid: { _eq: uuid } },
        },
        { affected_rows: true },
      ],
    },
    { operationName: "updateNotificationSeen" }
  );
};

export const getUnreadCount = async ({ uuid }: { uuid: string }) => {
  const currentCursor = await chain("query")(
    {
      auth_notification_cursor: [
        {
          where: { uuid: { _eq: uuid } },
        },
        {
          last_read_notificaiton: true,
        },
      ],
    },
    { operationName: "getUnreadCount" }
  );

  const lastReadNotificationId =
    currentCursor.auth_notification_cursor[0]?.last_read_notificaiton;

  const aggregationCounts = await chain("query")(
    {
      auth_notifications_aggregate: [
        {
          where: {
            uuid: { _eq: uuid },
            id: { _gt: lastReadNotificationId || 0 },
          },
        },
        {
          aggregate: {
            count: true,
          },
        },
      ],
    },
    { operationName: "getUnreadCount" }
  );
  return aggregationCounts.auth_notifications_aggregate.aggregate?.count;
};

export const getSubscriptions = async ({ uuid }: { uuid: string }) => {
  return chain("query")(
    {
      auth_notification_subscriptions: [
        { where: { uuid: { _eq: uuid } } },
        { id: true },
      ],
    },
    { operationName: "getSubscriptions" }
  );
};

export const deleteSubscriptions = async ({ uuid }: { uuid: string }) => {
  return chain("mutation")(
    {
      delete_auth_notification_subscriptions: [
        {
          where: {
            uuid: { _eq: uuid },
          },
        },
        {
          affected_rows: true,
        },
      ],
    },
    { operationName: "deleteSubscriptions" }
  );
};


