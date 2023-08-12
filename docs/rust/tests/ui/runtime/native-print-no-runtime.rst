tests/ui/runtime/native-print-no-runtime.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(start)]

#[start]
pub fn main(_: isize, _: *const *const u8) -> isize {
    println!("hello");
    0
}


