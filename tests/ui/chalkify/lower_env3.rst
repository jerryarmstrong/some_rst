tests/ui/chalkify/lower_env3.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

#![allow(dead_code)]

trait Foo {
    fn foo(&self);
}

impl<T> Foo for T where T: Clone {
    fn foo(&self) {
    }
}

fn main() {
}


