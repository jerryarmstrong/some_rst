tests/ui/generic-associated-types/gat-trait-path-generic-type-arg.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type F<'a>;

    fn identity<'a>(t: &'a Self::F<'a>) -> &'a Self::F<'a> { t }
}

impl <T, T1> Foo for T {
    //~^ ERROR: the type parameter `T1` is not constrained
    type F<T1> = &[u8];
      //~^ ERROR: the name `T1` is already used for
      //~| ERROR: `&` without an explicit lifetime name cannot be used here
}

fn main() {}


