tests/ui/unboxed-closures/unboxed-closure-sugar-wrong-trait.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unboxed_closures)]

trait Trait {}

fn f<F:Trait(isize) -> isize>(x: F) {}
//~^ ERROR this trait takes 0 generic arguments but 1 generic argument
//~| ERROR associated type `Output` not found for `Trait`

fn main() {}


