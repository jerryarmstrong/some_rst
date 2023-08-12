src/tools/miri/tests/fail/stacked_borrows/invalidate_against_protector1.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn inner(x: *mut i32, _y: &mut i32) {
    // If `x` and `y` alias, retagging is fine with this... but we really
    // shouldn't be allowed to use `x` at all because `y` was assumed to be
    // unique for the duration of this call.
    let _val = unsafe { *x }; //~ ERROR: protect
}

fn main() {
    let mut x = 0;
    let xraw = &mut x as *mut _;
    let xref = unsafe { &mut *xraw };
    inner(xraw, xref);
}


