ts/packages/anchor/src/utils/bytes/utf8.ts
==========================================

Last edited: 2022-12-14 20:15:57

Contents:

.. code-block:: ts

    import { isBrowser } from "../common";

export function decode(array: Uint8Array): string {
  const decoder = isBrowser
    ? new TextDecoder("utf-8") // Browser https://caniuse.com/textencoder.
    : new (require("util").TextDecoder)("utf-8"); // Node.

  return decoder.decode(array);
}

export function encode(input: string): Uint8Array {
  const encoder = isBrowser
    ? new TextEncoder() // Browser.
    : new (require("util").TextEncoder)("utf-8"); // Node.
  return encoder.encode(input);
}


