src/tools/miri/tests/fail/stacked_borrows/illegal_write5.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // A callee may not write to the destination of our `&mut` without us noticing.

fn main() {
    let mut x = 15;
    let xraw = &mut x as *mut _;
    // Derived from raw value, so using raw value is still ok ...
    let xref = unsafe { &mut *xraw };
    callee(xraw);
    // ... though any use of raw value will invalidate our ref.
    let _val = *xref;
    //~^ ERROR: /read access .* tag does not exist in the borrow stack/
}

fn callee(xraw: *mut i32) {
    unsafe { *xraw = 15 };
}


