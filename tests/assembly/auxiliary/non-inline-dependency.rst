tests/assembly/auxiliary/non-inline-dependency.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![no_std]
#![deny(warnings)]

#[inline(never)]
#[no_mangle]
pub fn wrapping_external_fn(a: u32) -> u32 {
    a.wrapping_mul(a)
}

#[inline(never)]
#[no_mangle]
pub fn panicking_external_fn(a: u32) -> u32 {
    a * a
}


