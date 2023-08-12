tests/ui/suggestions/issue-85943-no-suggest-unsized-indirection-in-where-clause.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #85943: should not emit suggestions for adding
// indirection to type parameters in where-clauses when suggesting
// adding `?Sized`.
struct A<T>(T) where T: Send;
struct B(A<[u8]>);
//~^ ERROR the size for values of type

pub fn main() {
}


