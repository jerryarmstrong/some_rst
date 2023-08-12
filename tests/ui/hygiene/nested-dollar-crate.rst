tests/ui/hygiene/nested-dollar-crate.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:nested-dollar-crate.rs
// edition:2018
// run-pass

extern crate nested_dollar_crate;

fn main() {
    assert_eq!(nested_dollar_crate::inner!(), "In def crate!");
}


