flow-typed/cbor.js
==================

Last edited: 2020-05-08 23:31:17

Contents:

.. code-block:: js

    declare module 'cbor' {
  declare module.exports: {
    decode(input: Buffer): Object;
    encode(input: any): Buffer;
  };
}


