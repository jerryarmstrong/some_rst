tests/ui/lint/trivial-cast-ice.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:trivial-cast-ice.rs
// check-pass

// Demonstrates the ICE in #102561

#![deny(trivial_casts)]

extern crate trivial_cast_ice;

fn main() {
    trivial_cast_ice::foo!();
}


