src/tools/miri/tests/fail/stacked_borrows/aliasing_mut3.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem;

pub fn safe(_x: &mut i32, _y: &i32) {} //~ ERROR: borrow stack

fn main() {
    let mut x = 0;
    let xref = &mut x;
    let xraw: *mut i32 = unsafe { mem::transmute_copy(&xref) };
    let xshr = &*xref;
    // transmute fn ptr around so that we can avoid retagging
    let safe_raw: fn(x: *mut i32, y: *const i32) =
        unsafe { mem::transmute::<fn(&mut i32, &i32), _>(safe) };
    safe_raw(xraw, xshr);
}


