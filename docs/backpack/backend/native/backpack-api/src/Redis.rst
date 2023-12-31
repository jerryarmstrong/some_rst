backend/native/backpack-api/src/Redis.ts
========================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { RedisClientType } from "redis";
import { createClient } from "redis";

import { NOTIFICATIONS_QUEUE, REDIS_URL } from "./config";

export class Redis {
  private client: RedisClientType;
  private static instance: Redis;

  constructor() {
    this.client = createClient({
      url: REDIS_URL,
    });
    this.client.connect();
  }

  public static getInstance(): Redis {
    if (!this.instance) {
      this.instance = new Redis();
    }
    return this.instance;
  }

  // TODO: debounce here
  async send(message: string) {
    await this.client.rPush(NOTIFICATIONS_QUEUE, message);
  }

  async publish(room: string, message: any) {
    await this.client.publish(room, JSON.stringify(message));
  }
}


