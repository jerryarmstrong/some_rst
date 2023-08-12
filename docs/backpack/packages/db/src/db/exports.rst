packages/db/src/db/exports.ts
=============================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export {
  bulkAddChats,
  clearChats,
  createOrUpdateCollection,
  deleteChat,
  latestReceivedMessage,
  latestReceivedUpdate,
  oldestReceivedMessage,
  processMessageUpdates,
  resetUpdateTimestamp,
} from "./chats";
export * from "./friends";
export * from "./images";
export { bulkAddUsers, getBulkUsers } from "./users";


