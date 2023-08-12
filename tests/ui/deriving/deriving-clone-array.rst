tests/ui/deriving/deriving-clone-array.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// test for issue #30244

#[derive(Copy, Clone)]
struct Array {
    arr: [[u8; 256]; 4]
}

pub fn main() {}


