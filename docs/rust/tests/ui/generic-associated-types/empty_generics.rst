tests/ui/generic-associated-types/empty_generics.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type Bar<,>;
    //~^ ERROR expected one of `#`, `>`, `const`, identifier, or lifetime, found `,`
}

fn main() {}


