tests/ui/suggestions/missing-assoc-fn.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait TraitB {
    type Item;
}

trait TraitA<A> {
    fn foo<T: TraitB<Item = A>>(_: T) -> Self;
    fn bar<T>(_: T) -> Self;
    fn baz<T>(_: T) -> Self where T: TraitB, <T as TraitB>::Item: Copy;
    fn bat<T: TraitB<Item: Copy>>(_: T) -> Self; //~ ERROR associated type bounds are unstable
}

struct S;

impl TraitA<()> for S { //~ ERROR not all trait items implemented
}

use std::iter::FromIterator;
struct X;
impl FromIterator<()> for X { //~ ERROR not all trait items implemented
}

fn main() {}


