tests/ui/consts/transmute-const.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::mem;

#[repr(transparent)]
struct Foo(#[allow(unused_tuple_struct_fields)] u32);

const TRANSMUTED_U32: u32 = unsafe { mem::transmute(Foo(3)) };

fn main() {
    assert_eq!(TRANSMUTED_U32, 3);
}


