tests/ui/optimization-fuel-0.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![crate_name="foo"]

use std::mem::size_of;

// compile-flags: -Z fuel=foo=0

#[allow(unused_tuple_struct_fields)]
struct S1(u8, u16, u8);
#[allow(unused_tuple_struct_fields)]
struct S2(u8, u16, u8);

fn main() {
    assert_eq!(size_of::<S1>(), 6);
    assert_eq!(size_of::<S2>(), 6);
}


