tests/ui/generic-associated-types/gat-trait-path-parenthesised-args.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait X {
  type Y<'a>;
}

fn foo<'a>(arg: Box<dyn X<Y('a) = &'a ()>>) {}
  //~^ ERROR: lifetime in trait object type must be followed by `+`
  //~| ERROR: parenthesized generic arguments cannot be used
  //~| ERROR this associated type takes 0 generic arguments but 1 generic argument
  //~| ERROR this associated type takes 1 lifetime argument but 0 lifetime arguments


fn bar<'a>(arg: Box<dyn X<Y() = ()>>) {}
  //~^ ERROR: parenthesized generic arguments cannot be used
  //~| ERROR this associated type takes 1 lifetime argument but 0 lifetime arguments

fn main() {}


