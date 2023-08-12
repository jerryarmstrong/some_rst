src/tools/miri/tests/fail/alloc/reallocate-change-alloc.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::alloc::{alloc, realloc, Layout};

fn main() {
    unsafe {
        let x = alloc(Layout::from_size_align_unchecked(1, 1));
        let _y = realloc(x, Layout::from_size_align_unchecked(1, 1), 1);
        let _z = *x; //~ ERROR: dereferenced after this allocation got freed
    }
}


