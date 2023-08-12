packages/chat-sdk/src/components/messageInput/replaceAt.ts
==========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export function replaceAt(
  str: string,
  replacement: string,
  index: number,
  length = 0
) {
  const prefix = str.substr(0, index);
  const suffix = str.substr(index + length);

  return prefix + replacement + suffix;
}


