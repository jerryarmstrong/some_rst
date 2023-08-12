src/tools/miri/tests/fail/intrinsics/unchecked_add1.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unchecked_math)]

fn main() {
    // MAX overflow
    let _val = unsafe { 40000u16.unchecked_add(30000) }; //~ ERROR: overflow executing `unchecked_add`
}


