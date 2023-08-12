packages/chat-sdk/src/utils/imageUploadUtils.ts
===============================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    export function base64ToArrayBuffer(base64: string) {
  base64 = base64.replace(/^data:([^;]+);base64,/gim, "");
  const binary = atob(base64);
  const len = binary.length;
  const buffer = new ArrayBuffer(len);
  const view = new Uint8Array(buffer);
  for (let i = 0; i < len; i++) {
    view[i] = binary.charCodeAt(i);
  }
  return buffer;
}


