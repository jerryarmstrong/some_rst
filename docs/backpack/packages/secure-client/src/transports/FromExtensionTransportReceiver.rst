packages/secure-client/src/transports/FromExtensionTransportReceiver.ts
=======================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import {
  CHANNEL_SECURE_BACKGROUND_EXTENSION_REQUEST,
  CHANNEL_SECURE_BACKGROUND_EXTENSION_RESPONSE,
  getLogger,
} from "@coral-xyz/common";
import { TransportResponder } from "@coral-xyz/secure-background/clients";
import type {
  SECURE_EVENTS,
  SecureRequest,
  SecureResponseType,
  TransportHandler,
  TransportReceiver,
} from "@coral-xyz/secure-background/types";

const logger = getLogger("secure-client FromExtensionTransportReceiver");

export class FromExtensionTransportReceiver<
  T extends SECURE_EVENTS = SECURE_EVENTS,
  R extends SecureResponseType = "response"
> implements TransportReceiver<T, R>
{
  constructor() {}

  public setHandler = (handler: TransportHandler<T, R>) => {
    const listener = async (message: {
      channel: string;
      data: SecureRequest<T>;
    }) => {
      if (message.channel !== CHANNEL_SECURE_BACKGROUND_EXTENSION_REQUEST) {
        return;
      }

      new TransportResponder<T, R>({
        request: message.data,
        handler,
        onResponse: (response) => {
          chrome.runtime
            .sendMessage({
              channel: CHANNEL_SECURE_BACKGROUND_EXTENSION_RESPONSE,
              data: response,
            })
            .catch((error) => {
              logger.error(error);
            });
        },
      });
    };
    chrome.runtime.onMessage.addListener(listener);
    return () => {
      chrome.runtime.onMessage.removeListener(listener);
    };
  };
}


