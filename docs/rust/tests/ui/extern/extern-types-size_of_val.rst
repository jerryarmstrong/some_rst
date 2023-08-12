tests/ui/extern/extern-types-size_of_val.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(extern_types)]

use std::mem::{align_of_val, size_of_val};

extern "C" {
    type A;
}

fn main() {
    let x: &A = unsafe { &*(1usize as *const A) };

    assert_eq!(size_of_val(x), 0);
    assert_eq!(align_of_val(x), 1);
}


