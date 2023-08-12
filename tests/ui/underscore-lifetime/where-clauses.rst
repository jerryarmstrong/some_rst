tests/ui/underscore-lifetime/where-clauses.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo<'a> {}

impl<'b: '_> Foo<'b> for i32 {} //~ ERROR `'_` cannot be used here

impl<T: '_> Foo<'static> for Vec<T> {} //~ ERROR `'_` cannot be used here

fn main() { }


