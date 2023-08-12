packages/library-legacy/src/utils/to-buffer.ts
==============================================

Last edited: 2023-08-11 09:49:26

Contents:

.. code-block:: ts

    import {Buffer} from 'buffer';

export const toBuffer = (arr: Buffer | Uint8Array | Array<number>): Buffer => {
  if (Buffer.isBuffer(arr)) {
    return arr;
  } else if (arr instanceof Uint8Array) {
    return Buffer.from(arr.buffer, arr.byteOffset, arr.byteLength);
  } else {
    return Buffer.from(arr);
  }
};


