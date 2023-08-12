tests/ui/chalkify/lower_struct.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

struct Foo<'a, T> where Box<T>: Clone {
    _x: std::marker::PhantomData<&'a T>,
}

fn main() { }


