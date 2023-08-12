tests/ui/unused-crate-deps/unused-aliases.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Warn about unused aliased for the crate

// edition:2018
// check-pass
// aux-crate:bar=bar.rs
// aux-crate:barbar=bar.rs

#![warn(unused_crate_dependencies)]
//~^ WARNING external crate `barbar` unused in

use bar as _;

fn main() {}


