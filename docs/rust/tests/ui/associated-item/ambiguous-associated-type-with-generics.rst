tests/ui/associated-item/ambiguous-associated-type-with-generics.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
trait Trait<A> {}

trait Assoc {
    type Ty;
}

impl<A> Assoc for dyn Trait<A> {
    type Ty = i32;
}

fn main() {
    let _x: <dyn Trait<i32>>::Ty; //~ ERROR ambiguous associated type
}


