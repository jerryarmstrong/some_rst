src/tools/miri/tests/fail/intrinsics/ptr_offset_int_plus_ptr.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-permissive-provenance

fn main() {
    let ptr = Box::into_raw(Box::new(0u32));
    // Can't start with an integer pointer and get to something usable
    unsafe {
        let _val = (1 as *mut u8).offset(ptr as isize); //~ERROR: is a dangling pointer
    }
}


