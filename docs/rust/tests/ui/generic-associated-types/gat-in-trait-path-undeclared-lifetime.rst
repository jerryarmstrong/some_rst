tests/ui/generic-associated-types/gat-in-trait-path-undeclared-lifetime.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X {
  type Y<'x>;
}

fn main() {
  fn _f(arg : Box<dyn for<'a> X<Y<'x> = &'a [u32]>>) {}
    //~^ ERROR: use of undeclared lifetime name `'x`
    //~| ERROR: binding for associated type `Y` references lifetime
}


