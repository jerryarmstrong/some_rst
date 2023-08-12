src/tools/miri/tests/fail/provenance/strict_provenance_cast.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-strict-provenance
#![feature(strict_provenance)]

fn main() {
    let addr = &0 as *const i32 as usize;
    let _ptr = std::ptr::from_exposed_addr::<i32>(addr); //~ ERROR: integer-to-pointer casts and `ptr::from_exposed_addr` are not supported
}


