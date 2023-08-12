tests/ui/suggestions/missing-assoc-fn-applicable-suggestions.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
trait TraitB {
    type Item;
}

trait TraitA<A> {
    type Type;
    fn bar<T>(_: T) -> Self;
    fn baz<T>(_: T) -> Self where T: TraitB, <T as TraitB>::Item: Copy;
}

struct S;
struct Type;

impl TraitA<()> for S { //~ ERROR not all trait items implemented
}

fn main() {}


