packages/secure-background/src/services/evm/events.ts
=====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { SecureEventBase } from "../../types/transports";

// Also add new events to: ../../events.ts

export type SECURE_EVM_EVENTS =
  | "SECURE_EVM_SIGN_MESSAGE"
  | "SECURE_EVM_SIGN_TX";

export interface SECURE_EVM_SIGN_MESSAGE
  extends SecureEventBase<"SECURE_EVM_SIGN_MESSAGE"> {
  request: {
    message: string;
    publicKey: string;
  };
  response: {
    singedMessage: string;
  };
}

export interface SECURE_EVM_SIGN_TX
  extends SecureEventBase<"SECURE_EVM_SIGN_TX"> {
  request: {
    publicKey: string;
    tx: string;
  };
  response: {
    signedTx: string;
  };
}


