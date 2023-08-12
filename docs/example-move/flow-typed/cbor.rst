flow-typed/cbor.js
==================

Last edited: 2020-07-29 22:45:43

Contents:

.. code-block:: js

    declare module 'cbor' {
  declare module.exports: {
    decode(input: Buffer): Object;
    encode(input: any): Buffer;
  };
}


