src/tools/miri/tests/fail/invalid_enum_tag.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Validation makes this fail in the wrong place
// Make sure we find these even with many checks disabled.
//@compile-flags: -Zmiri-disable-alignment-check -Zmiri-disable-stacked-borrows -Zmiri-disable-validation

use std::mem;

#[repr(C)]
pub enum Foo {
    A,
    B,
    C,
    D,
}

fn main() {
    let f = unsafe { std::mem::transmute::<i32, Foo>(42) };
    let _val = mem::discriminant(&f); //~ERROR: enum value has invalid tag
}


