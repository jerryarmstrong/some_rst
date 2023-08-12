src/tools/miri/tests/fail/stacked_borrows/invalidate_against_protector3.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::alloc::{alloc, Layout};

fn inner(x: *mut i32, _y: &i32) {
    // If `x` and `y` alias, retagging is fine with this... but we really
    // shouldn't be allowed to write to `x` at all because `y` was assumed to be
    // immutable for the duration of this call.
    unsafe { *x = 0 }; //~ ERROR: protect
}

fn main() {
    unsafe {
        let ptr = alloc(Layout::for_value(&0i32)) as *mut i32;
        inner(ptr, &*ptr);
    };
}


