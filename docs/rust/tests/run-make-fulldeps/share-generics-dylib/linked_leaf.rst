tests/run-make-fulldeps/share-generics-dylib/linked_leaf.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate instance_user_dylib;
extern crate instance_user_a_rlib;
extern crate instance_user_b_rlib;

use std::cell::Cell;

fn main() {

    instance_user_a_rlib::foo();
    instance_user_b_rlib::foo();
    instance_user_dylib::foo();

    let a: Cell<i32> = Cell::new(1);
    a.set(123);
}


