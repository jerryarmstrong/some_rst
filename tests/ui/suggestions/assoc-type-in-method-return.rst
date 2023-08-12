tests/ui/suggestions/assoc-type-in-method-return.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A {
    type Bla;
    fn to_bla(&self) -> Bla;
    //~^ ERROR cannot find type `Bla` in this scope
}

fn main() {}


