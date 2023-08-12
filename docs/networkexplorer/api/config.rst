api/config.js
=============

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    export default {
  service: {
    tcp: false,
    udp: false,
    unixds: true,
    host: '127.0.0.1',
    port: 7654,
    socket: '/tmp/solana-blockstream.sock',
  },
  redis: {
    host: '127.0.0.1',
    port: 6379,
    // path: '/var/run/redis/redis-server.sock',
  },
};


