tests/ui/chalkify/lower_env1.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

#![allow(dead_code)]

trait Foo { }

trait Bar where Self: Foo { }

fn bar<T: Bar + ?Sized>() {
}

fn main() {
}


