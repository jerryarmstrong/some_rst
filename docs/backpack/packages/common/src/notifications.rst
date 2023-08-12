packages/common/src/notifications.ts
====================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export interface EnrichedNotification extends DbNotification {
  xnftImage: string;
  xnftTitle: string;
}

export interface DbNotification {
  title: string;
  body: string;
  xnft_id: string;
  timestamp: number;
  id: number;
  viewed: boolean;
}

export type GroupedNotification = {
  date: string;
  notifications: EnrichedNotification[];
};


