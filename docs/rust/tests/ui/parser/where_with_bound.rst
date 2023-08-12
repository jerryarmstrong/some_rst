tests/ui/parser/where_with_bound.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T>() where <T>::Item: ToString, T: Iterator { }
//~^ ERROR generic parameters on `where` clauses are reserved for future use
//~| ERROR cannot find type `Item` in the crate root

fn main() {}


