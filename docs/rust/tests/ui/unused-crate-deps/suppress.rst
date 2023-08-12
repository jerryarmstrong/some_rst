tests/ui/unused-crate-deps/suppress.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Suppress by using crate

// edition:2018
// check-pass
// aux-crate:bar=bar.rs

#![warn(unused_crate_dependencies)]

use bar as _;

fn main() {}


