src/tools/miri/tests/fail/intrinsics/unchecked_add2.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unchecked_math)]

fn main() {
    // MIN overflow
    let _val = unsafe { (-30000i16).unchecked_add(-8000) }; //~ ERROR: overflow executing `unchecked_add`
}


