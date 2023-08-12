tests/ui/suggestions/suggest-ref-macro.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-check
// aux-build:proc-macro-type-error.rs

extern crate proc_macro_type_error;

use proc_macro_type_error::hello;

#[hello] //~ERROR mismatched types
fn abc() {}

fn x(_: &mut i32) {}

macro_rules! bla {
    () => {
        x(123);
        //~^ ERROR mismatched types
        //~| SUGGESTION &mut 123
    };
    ($v:expr) => {
        x($v)
    }
}

fn main() {
    bla!();
    bla!(456);
    //~^ ERROR mismatched types
    //~| SUGGESTION &mut 456
}


