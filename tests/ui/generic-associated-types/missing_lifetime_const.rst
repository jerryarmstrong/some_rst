tests/ui/generic-associated-types/missing_lifetime_const.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type Assoc<'a, const N: usize>;
}

fn foo<T: Foo>() {
    let _: <T as Foo>::Assoc<3>;
      //~^ ERROR  this associated type
}

fn main() {}


