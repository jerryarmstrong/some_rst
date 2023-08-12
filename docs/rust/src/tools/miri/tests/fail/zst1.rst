src/tools/miri/tests/fail/zst1.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // make sure ZST locals cannot be accessed
    let x = &() as *const () as *const i8;
    let _val = unsafe { *x }; //~ ERROR: out-of-bounds
}


