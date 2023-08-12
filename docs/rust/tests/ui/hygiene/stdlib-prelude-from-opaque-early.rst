tests/ui/hygiene/stdlib-prelude-from-opaque-early.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:stdlib-prelude.rs

#![feature(decl_macro)]
#![feature(prelude_import)]

extern crate stdlib_prelude;

#[prelude_import]
use stdlib_prelude::*;

macro mac() {
    mod m {
        use std::mem; // OK (extern prelude)
        stdlib_macro!(); // OK (stdlib prelude)
    }
}

mac!();

fn main() {}


