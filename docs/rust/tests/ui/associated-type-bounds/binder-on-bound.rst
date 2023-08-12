tests/ui/associated-type-bounds/binder-on-bound.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait {
    type Bound<'a>;
}

fn foo() where Trait<for<'a> Bound<'a> = &'a ()> {
    //~^ ERROR `for<...>` is not allowed on associated type bounds
}

fn main() {}


