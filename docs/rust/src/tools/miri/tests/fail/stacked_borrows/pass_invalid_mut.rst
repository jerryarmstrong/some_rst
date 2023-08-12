src/tools/miri/tests/fail/stacked_borrows/pass_invalid_mut.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure that we cannot pass by argument a `&mut` that got already invalidated.
fn foo(_: &mut i32) {}

fn main() {
    let x = &mut 42;
    let xraw = x as *mut _;
    let xref = unsafe { &mut *xraw };
    let _val = unsafe { *xraw }; // invalidate xref
    foo(xref); //~ ERROR: /retag .* tag does not exist in the borrow stack/
}


