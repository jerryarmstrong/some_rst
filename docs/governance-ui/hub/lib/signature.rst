hub/lib/signature.ts
====================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: ts

    export function toHex(signature: Uint8Array) {
  return Array.from(signature)
    .map((n) => n.toString(16).padStart(2, '0'))
    .join('');
}

export function toUint8Array(msg: string) {
  return new TextEncoder().encode(msg);
}


