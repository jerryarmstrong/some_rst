src/tools/miri/tests/fail/alloc/reallocate-bad-size.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::alloc::{alloc, realloc, Layout};

//@error-pattern: has size 1 and alignment 1, but gave size 2 and alignment 1

fn main() {
    unsafe {
        let x = alloc(Layout::from_size_align_unchecked(1, 1));
        let _y = realloc(x, Layout::from_size_align_unchecked(2, 1), 1);
    }
}


