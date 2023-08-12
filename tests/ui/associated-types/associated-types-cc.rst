tests/ui/associated-types/associated-types-cc.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
// aux-build:associated-types-cc-lib.rs

// Test that we are able to reference cross-crate traits that employ
// associated types.

extern crate associated_types_cc_lib as bar;

use bar::Bar;

fn foo<B:Bar>(b: B) -> <B as Bar>::T {
    Bar::get(None::<B>)
}

fn main() {
    println!("{}", foo(3));
}


