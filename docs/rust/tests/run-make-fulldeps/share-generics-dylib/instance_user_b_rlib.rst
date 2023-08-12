tests/run-make-fulldeps/share-generics-dylib/instance_user_b_rlib.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate instance_provider_b as upstream;
use std::cell::Cell;

pub fn foo() {
    upstream::foo();

    let b: Cell<i32> = Cell::new(1);
    b.set(123);
}


