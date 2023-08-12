tests/ui/dyn-keyword/dyn-2018-edition-lint.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
#[deny(bare_trait_objects)]

fn function(x: &SomeTrait, y: Box<SomeTrait>) {
    //~^ ERROR trait objects without an explicit `dyn` are deprecated
    //~| WARN this is accepted in the current edition
    //~| ERROR trait objects without an explicit `dyn` are deprecated
    //~| WARN this is accepted in the current edition
    //~| ERROR trait objects without an explicit `dyn` are deprecated
    //~| WARN this is accepted in the current edition
    //~| ERROR trait objects without an explicit `dyn` are deprecated
    //~| WARN this is accepted in the current edition
    //~| ERROR trait objects without an explicit `dyn` are deprecated
    //~| WARN this is accepted in the current edition
    //~| ERROR trait objects without an explicit `dyn` are deprecated
    //~| WARN this is accepted in the current edition
    let _x: &SomeTrait = todo!();
    //~^ ERROR trait objects without an explicit `dyn` are deprecated
    //~| WARN this is accepted in the current edition
}

trait SomeTrait {}

fn main() {}


