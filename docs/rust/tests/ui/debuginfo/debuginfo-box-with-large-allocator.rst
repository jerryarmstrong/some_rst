tests/ui/debuginfo/debuginfo-box-with-large-allocator.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
// compile-flags: -Cdebuginfo=2
// fixes issue #94725

#![feature(allocator_api)]

use std::alloc::{AllocError, Allocator, Layout};
use std::ptr::NonNull;

struct ZST;

unsafe impl Allocator for &ZST {
    fn allocate(&self, layout: Layout) -> Result<NonNull<[u8]>, AllocError> {
        todo!()
    }
    unsafe fn deallocate(&self, ptr: NonNull<u8>, layout: Layout) {
        todo!()
    }
}

fn main() {
    let _ = Box::<i32, &ZST>::new_in(43, &ZST);
}


