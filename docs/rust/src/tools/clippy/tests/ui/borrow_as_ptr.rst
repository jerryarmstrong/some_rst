src/tools/clippy/tests/ui/borrow_as_ptr.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![warn(clippy::borrow_as_ptr)]

fn main() {
    let val = 1;
    let _p = &val as *const i32;

    let mut val_mut = 1;
    let _p_mut = &mut val_mut as *mut i32;
}


