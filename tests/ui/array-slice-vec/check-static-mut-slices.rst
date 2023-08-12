tests/ui/array-slice-vec/check-static-mut-slices.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

// Checks that mutable static items can have mutable slices


static mut TEST: &'static mut [isize] = &mut [1];
static mut EMPTY: &'static mut [isize] = &mut [];

pub fn main() {
    unsafe {
        TEST[0] += 1;
        assert_eq!(TEST[0], 2);
    }
}


