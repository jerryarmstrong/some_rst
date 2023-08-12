packages/secure-background/src/transports/combineBroadcastTransportSenders.ts
=============================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { SECURE_EVENTS } from "../types/events";
import type { TransportSender } from "../types/transports";

export function combineBroadcastTransportSenders<
  T extends SECURE_EVENTS = SECURE_EVENTS
>(...clients: TransportSender<T>[]): TransportSender<T> {
  return {
    send: async (request) => {
      await Promise.all(clients.map(async (client) => client.send(request)));
      return Promise.resolve(true as any); // no response handling when broadcasting
    },
  };
}


