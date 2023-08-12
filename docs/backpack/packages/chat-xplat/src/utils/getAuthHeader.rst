packages/chat-xplat/src/utils/getAuthHeader.ts
==============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export const getAuthHeader = (
  jwt?: string
): {
  Authorization?: string;
} => {
  if (jwt) {
    return {
      Authorization: `Bearer ${jwt}`,
    };
  }
  return {};
};


