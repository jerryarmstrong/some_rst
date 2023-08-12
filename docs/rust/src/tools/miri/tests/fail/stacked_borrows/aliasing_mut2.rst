src/tools/miri/tests/fail/stacked_borrows/aliasing_mut2.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem;

pub fn safe(_x: &i32, _y: &mut i32) {} //~ ERROR: protect

fn main() {
    let mut x = 0;
    let xref = &mut x;
    let xraw: *mut i32 = unsafe { mem::transmute_copy(&xref) };
    let xshr = &*xref;
    // transmute fn ptr around so that we can avoid retagging
    let safe_raw: fn(x: *const i32, y: *mut i32) =
        unsafe { mem::transmute::<fn(&i32, &mut i32), _>(safe) };
    safe_raw(xshr, xraw);
}


