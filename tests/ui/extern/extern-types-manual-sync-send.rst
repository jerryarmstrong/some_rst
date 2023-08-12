tests/ui/extern/extern-types-manual-sync-send.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that unsafe impl for Sync/Send can be provided for extern types.

#![feature(extern_types)]

extern "C" {
    type A;
}

unsafe impl Sync for A {}
unsafe impl Send for A {}

fn assert_sync<T: ?Sized + Sync>() {}
fn assert_send<T: ?Sized + Send>() {}

fn main() {
    assert_sync::<A>();
    assert_send::<A>();
}


