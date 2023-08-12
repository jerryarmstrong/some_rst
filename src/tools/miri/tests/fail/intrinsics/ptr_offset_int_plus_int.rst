src/tools/miri/tests/fail/intrinsics/ptr_offset_int_plus_int.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-permissive-provenance

fn main() {
    // Can't offset an integer pointer by non-zero offset.
    unsafe {
        let _val = (1 as *mut u8).offset(1); //~ERROR: is a dangling pointer
    }
}


