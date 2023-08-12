packages/secure-background/src/services/user/client.ts
======================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { TransportSender } from "../../types/transports";

import type {
  SECURE_USER_APPROVE_ORIGIN,
  SECURE_USER_GET,
  SECURE_USER_REMOVE_ORIGIN,
  SECURE_USER_UNLOCK_KEYRING,
} from "./events";

export class UserClient {
  constructor(private secureBackgroundClient: TransportSender) {}

  public async unlockKeyring(
    request: SECURE_USER_UNLOCK_KEYRING["request"] = {}
  ) {
    return this.secureBackgroundClient.send({
      name: "SECURE_USER_UNLOCK_KEYRING",
      request,
    });
  }

  public async getUser(request: SECURE_USER_GET["request"] = {}) {
    return this.secureBackgroundClient.send({
      name: "SECURE_USER_GET",
      request,
    });
  }

  public async approveOrigin(request: SECURE_USER_APPROVE_ORIGIN["request"]) {
    return this.secureBackgroundClient.send({
      name: "SECURE_USER_APPROVE_ORIGIN",
      request,
    });
  }

  public async removeOrigin(request: SECURE_USER_REMOVE_ORIGIN["request"]) {
    return this.secureBackgroundClient.send({
      name: "SECURE_USER_REMOVE_ORIGIN",
      request,
    });
  }
}


