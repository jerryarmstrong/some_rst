tests/ui/macros/dollar-crate-nested-encoding.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:dollar-crate-nested-encoding.rs

extern crate dollar_crate_nested_encoding;

type A = dollar_crate_nested_encoding::exported!();

fn main() {}


