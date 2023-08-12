rpc-cache-utils/src/redisClient.ts
==================================

Last edited: 2021-08-05 17:33:45

Contents:

.. code-block:: ts

    import redis from "redis";

export enum RedisClientUser {
	Reader,
	Writer
};

export const getRedisClient = (clientType : RedisClientUser): redis.RedisClient => {
  if (process.env.ENV?.toLowerCase() === "aws") {
    return redis.createClient(
      clientType === RedisClientUser.Reader ? `${process.env.REDIS_SERVER_READ_URL}:${process.env.REDIS_SERVER_PORT}` :
	      				      `${process.env.REDIS_SERVER_PRIMARY_URL}:${process.env.REDIS_SERVER_PORT}`
    );
  } else {
    return redis.createClient();
  }
};


