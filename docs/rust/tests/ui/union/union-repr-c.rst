tests/ui/union/union-repr-c.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(unused)]
#![deny(improper_ctypes)]

#[repr(C)]
union U {
    a: u8,
}

union W {
    a: u8,
}

extern "C" {
    static FOREIGN1: U; // OK
    static FOREIGN2: W; //~ ERROR `extern` block uses type `W`
}

fn main() {}


