tests/ui/generic-associated-types/gat-trait-path-missing-lifetime.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X {
  type Y<'a>;

  fn foo<'a>(t : Self::Y<'a>) -> Self::Y<'a> { t }
}

impl<T> X for T {
  fn foo<'a, T1: X<Y = T1>>(t : T1) -> T1::Y<'a> {
    //~^ ERROR missing generics for associated type
    //~^^ ERROR missing generics for associated type
    t
  }
}

fn main() {}


