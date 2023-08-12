tests/ui/parser/misspelled-macro-rules.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #91227.

// run-rustfix

#![allow(unused_macros)]

marco_rules! thing {
//~^ ERROR: expected one of
//~| HELP: perhaps you meant to define a macro
    () => {}
}

fn main() {}


