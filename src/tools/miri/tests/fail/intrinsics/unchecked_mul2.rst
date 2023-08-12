src/tools/miri/tests/fail/intrinsics/unchecked_mul2.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unchecked_math)]
fn main() {
    // MIN overflow
    let _val = unsafe { 1_000_000_000i32.unchecked_mul(-4) }; //~ ERROR: overflow executing `unchecked_mul`
}


