src/tools/miri/tests/fail/intrinsics/unchecked_sub1.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unchecked_math)]
fn main() {
    // MIN overflow
    let _val = unsafe { 14u32.unchecked_sub(22) }; //~ ERROR: overflow executing `unchecked_sub`
}


