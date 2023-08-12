src/tools/miri/tests/fail/stacked_borrows/illegal_dealloc1.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@error-pattern: /deallocation .* tag does not exist in the borrow stack/
use std::alloc::{alloc, dealloc, Layout};

fn main() {
    unsafe {
        let x = alloc(Layout::from_size_align_unchecked(1, 1));
        let ptr1 = (&mut *x) as *mut u8;
        let ptr2 = (&mut *ptr1) as *mut u8;
        // Invalidate ptr2 by writing to ptr1.
        ptr1.write(0);
        // Deallocate through ptr2.
        dealloc(ptr2, Layout::from_size_align_unchecked(1, 1));
    }
}


