tests/ui/extern/extern-types-not-sync-send.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure extern types are !Sync and !Send.

#![feature(extern_types)]

extern "C" {
    type A;
}

fn assert_sync<T: ?Sized + Sync>() {}
fn assert_send<T: ?Sized + Send>() {}

fn main() {
    assert_sync::<A>();
    //~^ ERROR `A` cannot be shared between threads safely [E0277]

    assert_send::<A>();
    //~^ ERROR `A` cannot be sent between threads safely [E0277]
}


