flow-typed/cbor.js
==================

Last edited: 2020-06-24 17:49:11

Contents:

.. code-block:: js

    declare module 'cbor' {
  declare module.exports: {
    decode(input: Buffer): Object;
    encode(input: any): Buffer;
  };
}


