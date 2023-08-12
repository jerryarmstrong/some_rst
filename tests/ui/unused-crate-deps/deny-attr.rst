tests/ui/unused-crate-deps/deny-attr.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check for unused crate dep, no path

// edition:2018
// aux-crate:bar=bar.rs

#![deny(unused_crate_dependencies)]
//~^ ERROR external crate `bar` unused in

fn main() {}


