src/tools/miri/tests/fail/stacked_borrows/issue-miri-1050-2.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@error-pattern: is a dangling pointer
use std::ptr::NonNull;

fn main() {
    unsafe {
        let ptr = NonNull::<i32>::dangling();
        drop(Box::from_raw(ptr.as_ptr()));
    }
}


