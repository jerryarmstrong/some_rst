packages/chat-xplat/src/utils/getSanitizedTitle.ts
==================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    import type { MessageKind } from "@coral-xyz/common";
import { MessageWithMetadata } from "@coral-xyz/common";

export const getSanitizedTitle = (message: {
  message: string;
  message_kind: MessageKind;
}) => {
  return message.message_kind === "gif"
    ? "GIF"
    : message.message_kind === "secure-transfer"
    ? "Secure Transfer"
    : message.message_kind === "media"
    ? "Media"
    : message.message;
};


