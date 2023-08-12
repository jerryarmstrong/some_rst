tests/ui/generic-associated-types/unsatisfied-outlives-bound.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait ATy {
    type Item<'a>: 'a;
}

impl<'b> ATy for &'b () {
    type Item<'a> = &'b ();
    //~^ ERROR  the type `&'b ()` does not fulfill the required lifetime
}

trait StaticTy {
    type Item<'a>: 'static;
}

impl StaticTy for () {
    type Item<'a> = &'a ();
    //~^ ERROR  the type `&'a ()` does not fulfill the required lifetime
}

fn main() {}


