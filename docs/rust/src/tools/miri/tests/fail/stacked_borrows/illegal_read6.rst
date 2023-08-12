src/tools/miri/tests/fail/stacked_borrows/illegal_read6.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Creating a shared reference does not leak the data to raw pointers.
fn main() {
    unsafe {
        let x = &mut 0;
        let raw = x as *mut _;
        let x = &mut *x; // kill `raw`
        let _y = &*x; // this should not activate `raw` again
        let _val = *raw; //~ ERROR: /read access .* tag does not exist in the borrow stack/
    }
}


