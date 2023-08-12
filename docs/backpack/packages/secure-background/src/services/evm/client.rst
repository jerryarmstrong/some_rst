packages/secure-background/src/services/evm/client.ts
=====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { SecureRequest, TransportSender } from "../../types/transports";

export class EVMClient {
  constructor(private secureBackgroundClient: TransportSender) {}

  public async signMessage(
    request: SecureRequest<"SECURE_EVM_SIGN_MESSAGE">["request"]
  ) {
    await this.secureBackgroundClient.send({
      name: "SECURE_EVM_SIGN_MESSAGE",
      request,
    });
  }
}


