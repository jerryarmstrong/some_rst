tests/ui/chalkify/lower_impl.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

trait Foo { }

impl<T: 'static> Foo for T where T: Iterator<Item = i32> { }

trait Bar {
    type Assoc;
}

impl<T> Bar for T where T: Iterator<Item = i32> {
    type Assoc = Vec<T>;
}

fn main() {
}


