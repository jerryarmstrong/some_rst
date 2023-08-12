tests/ui/match/match-tag-nullary.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum A { A }
enum B { B }

fn main() { let x: A = A::A; match x { B::B => { } } } //~ ERROR mismatched types


