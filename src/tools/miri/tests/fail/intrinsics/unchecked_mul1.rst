src/tools/miri/tests/fail/intrinsics/unchecked_mul1.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unchecked_math)]
fn main() {
    // MAX overflow
    let _val = unsafe { 300u16.unchecked_mul(250u16) }; //~ ERROR: overflow executing `unchecked_mul`
}


