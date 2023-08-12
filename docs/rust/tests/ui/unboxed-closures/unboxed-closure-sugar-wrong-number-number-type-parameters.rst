tests/ui/unboxed-closures/unboxed-closure-sugar-wrong-number-number-type-parameters.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unboxed_closures)]

trait Zero { fn dummy(&self); }

fn foo1(_: dyn Zero()) {
    //~^ ERROR this trait takes 0 generic arguments but 1 generic argument
    //~| ERROR associated type `Output` not found for `Zero`
}

fn foo2(_: dyn Zero<usize>) {
    //~^ ERROR this trait takes 0 generic arguments but 1 generic argument
}

fn foo3(_: dyn Zero <   usize   >) {
    //~^ ERROR this trait takes 0 generic arguments but 1 generic argument
}

fn foo4(_: dyn Zero(usize)) {
    //~^ ERROR this trait takes 0 generic arguments but 1 generic argument
    //~| ERROR associated type `Output` not found for `Zero`
}

fn foo5(_: dyn Zero (   usize   )) {
    //~^ ERROR this trait takes 0 generic arguments but 1 generic argument
    //~| ERROR associated type `Output` not found for `Zero`
}

fn main() { }


