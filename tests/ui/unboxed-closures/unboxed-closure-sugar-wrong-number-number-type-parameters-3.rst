tests/ui/unboxed-closures/unboxed-closure-sugar-wrong-number-number-type-parameters-3.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unboxed_closures)]

trait Three<A,B,C> { fn dummy(&self) -> (A,B,C); }

fn foo(_: &dyn Three())
//~^ ERROR this trait takes 3 generic arguments but 1 generic argument
//~| ERROR associated type `Output` not found
{}

fn main() { }


