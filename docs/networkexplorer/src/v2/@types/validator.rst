src/v2/@types/validator.js
==========================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    // @flow

export type Identity = {
  avatarUrl: string,
  details: string,
  keybaseUsername: string,
  name: string,
  pubkey: string,
  verified: string,
  verifyUrl: string,
  website: string,
};

export type UptimeItem = {
  creditsEarned: number,
  epoch: number,
  percentage: string,
  slotsInEpoch: number,
};

export type Uptime = {
  lat: number,
  ts: number,
  votePubkey: string,
  uptime: UptimeItem[],
};

export type Validator = {
  commission: number,
  coordinated: [number, number],
  gossip: string,
  identity: Identity,
  nodePubkey: string,
  stake: number,
  uptime: Uptime,
};


