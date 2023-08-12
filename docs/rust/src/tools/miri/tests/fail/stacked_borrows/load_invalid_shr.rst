src/tools/miri/tests/fail/stacked_borrows/load_invalid_shr.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure we catch this even without validation
//@compile-flags: -Zmiri-disable-validation

// Make sure that we cannot load from memory a `&` that got already invalidated.
fn main() {
    let x = &mut 42;
    let xraw = x as *mut _;
    let xref = unsafe { &*xraw };
    let xref_in_mem = Box::new(xref);
    unsafe { *xraw = 42 }; // unfreeze
    let _val = *xref_in_mem; //~ ERROR: /retag .* tag does not exist in the borrow stack/
}


