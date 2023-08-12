tests/ui/chalkify/lower_trait.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

trait Bar { }

trait Foo<S, T: ?Sized> {
    type Assoc: Bar + ?Sized;
}

fn main() {
}


