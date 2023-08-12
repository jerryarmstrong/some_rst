tests/ui/unused-crate-deps/warn-attr.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check for unused crate dep, no path

// edition:2018
// check-pass
// aux-crate:bar=bar.rs

#![warn(unused_crate_dependencies)]
//~^ WARNING external crate `bar` unused in

fn main() {}


