tests/ui/traits/alias/import-cross-crate.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:greeter.rs

#![feature(trait_alias)]

extern crate greeter;

// Import only the alias, not the real trait.
use greeter::{Greet, Hi};

fn main() {
    let hi = Hi;
    hi.hello(); // From `Hello`, via `Greet` alias.
}


