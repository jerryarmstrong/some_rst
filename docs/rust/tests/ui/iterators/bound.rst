tests/ui/iterators/bound.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S<I: Iterator>(I);
struct T(S<u8>);
//~^ ERROR is not an iterator
fn main() {}


