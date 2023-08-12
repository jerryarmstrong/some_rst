library/std/src/sys/windows/alloc/tests.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use super::{Header, MIN_ALIGN};
use crate::mem;

#[test]
fn alloc_header() {
    // Header must fit in the padding before an aligned pointer
    assert!(mem::size_of::<Header>() <= MIN_ALIGN);
    assert!(mem::align_of::<Header>() <= MIN_ALIGN);
}


