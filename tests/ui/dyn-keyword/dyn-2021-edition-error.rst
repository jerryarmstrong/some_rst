tests/ui/dyn-keyword/dyn-2021-edition-error.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

fn function(x: &SomeTrait, y: Box<SomeTrait>) {
    //~^ ERROR trait objects must include the `dyn` keyword
    //~| ERROR trait objects must include the `dyn` keyword
    let _x: &SomeTrait = todo!();
}

trait SomeTrait {}

fn main() {}


