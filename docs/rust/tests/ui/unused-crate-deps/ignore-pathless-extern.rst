tests/ui/unused-crate-deps/ignore-pathless-extern.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Pathless --extern references don't count

// edition:2018
// check-pass
// aux-crate:bar=bar.rs
// compile-flags:--extern proc_macro

#![warn(unused_crate_dependencies)]

use bar as _;

fn main() {}


