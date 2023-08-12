src/tools/miri/tests/fail/provenance/ptr_invalid_offset.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-strict-provenance
#![feature(strict_provenance)]

fn main() {
    let x = 22;
    let ptr = &x as *const _ as *const u8;
    let roundtrip = std::ptr::invalid::<u8>(ptr as usize);
    // Not even offsetting this is allowed.
    let _ = unsafe { roundtrip.offset(1) }; //~ERROR: is a dangling pointer
}


