packages/chat-sdk/src/components/messageInput/isValidUsername.ts
================================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export function isValidUsername(username: string) {
  return /^@\w{1,15}$/.test(username);
}


