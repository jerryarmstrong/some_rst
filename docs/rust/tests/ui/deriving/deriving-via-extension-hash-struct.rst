tests/ui/deriving/deriving-via-extension-hash-struct.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

#[derive(Hash)]
struct Foo {
    x: isize,
    y: isize,
    z: isize
}

pub fn main() {}


