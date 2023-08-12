tests/codegen/src-hash-algorithm/src-hash-algorithm-sha1.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -g -Z src-hash-algorithm=sha1

#![crate_type = "lib"]

pub fn test() {}
// CHECK: checksumkind: CSK_SHA1


