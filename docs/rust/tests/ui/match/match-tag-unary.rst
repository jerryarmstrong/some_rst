tests/ui/match/match-tag-unary.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum A { A(isize) }
enum B { B(isize) }

fn main() { let x: A = A::A(0); match x { B::B(y) => { } } } //~ ERROR mismatched types


