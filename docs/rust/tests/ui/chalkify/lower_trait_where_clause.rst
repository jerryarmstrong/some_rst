tests/ui/chalkify/lower_trait_where_clause.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

use std::borrow::Borrow;

trait Foo<'a, 'b, T, U>
where
    T: Borrow<U> + ?Sized,
    U: ?Sized + 'b,
    'a: 'b,
    Box<T>:, // NOTE(#53696) this checks an empty list of bounds.
{
}

fn main() {
}


