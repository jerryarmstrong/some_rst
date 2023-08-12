src/tools/miri/tests/fail/alloc/deallocate-bad-alignment.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::alloc::{alloc, dealloc, Layout};

//@error-pattern: has size 1 and alignment 1, but gave size 1 and alignment 2

fn main() {
    unsafe {
        let x = alloc(Layout::from_size_align_unchecked(1, 1));
        dealloc(x, Layout::from_size_align_unchecked(1, 2));
    }
}


