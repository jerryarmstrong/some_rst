src/tools/miri/tests/pass/disable-alignment-check.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-disable-alignment-check

fn main() {
    let mut x = [0u8; 20];
    let x_ptr: *mut u8 = x.as_mut_ptr();
    // At least one of these is definitely unaligned.
    unsafe {
        *(x_ptr as *mut u64) = 42;
        *(x_ptr.add(1) as *mut u64) = 42;
    }
}


