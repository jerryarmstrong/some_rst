ts/packages/anchor/src/utils/bytes/base64.ts
============================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { Buffer } from "buffer";
import * as base64 from "base64-js";

export function encode(data: Buffer): string {
  return base64.fromByteArray(data);
}

export function decode(data: string): Buffer {
  return Buffer.from(base64.toByteArray(data));
}


